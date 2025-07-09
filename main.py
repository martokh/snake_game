from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import turtle
import os

screen = turtle.Screen()
screen.setup(width=650, height=550)

SCORE_FILE = "alltime_scores.txt"

# Helper to load and save scores
def load_scores():
    if not os.path.exists(SCORE_FILE):
        return []
    with open(SCORE_FILE, "r") as f:
        return [int(line.strip()) for line in f if line.strip().isdigit()]

def save_score(score):
    scores = load_scores()
    scores.append(score)
    with open(SCORE_FILE, "w") as f:
        for s in sorted(scores, reverse=True)[:100]:
            f.write(f"{s}\n")

def show_scoreboard(screen, last_score):
    # Clear all turtles (snake, food, etc.)
    for t in screen.turtles():
        t.hideturtle()
        t.clear()
    screen.update()
    # Draw larger scoreboard background
    board = turtle.Turtle()
    board.hideturtle()
    board.penup()
    rect_width = 370
    rect_height = 340
    board.goto(-rect_width//2, 90)
    board.pendown()
    board.fillcolor("#222")
    board.pencolor("#00FF99")
    board.pensize(3)
    board.begin_fill()
    for _ in range(2):
        board.forward(rect_width)
        board.right(90)
        board.forward(rect_height)
        board.right(90)
    board.end_fill()
    board.penup()
    # Draw GAME OVER
    y = 70
    board.goto(0, y)
    board.color("#FF3333")
    board.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
    # Draw Top 5 Scores
    y -= 50
    board.goto(0, y)
    board.color("#00FF99")
    board.write("TOP 5 SCORES", align="center", font=("Arial", 26, "bold"))
    # Draw score list
    scores = load_scores()
    top_scores = sorted(scores, reverse=True)[:5]
    y -= 35
    board.color("white")
    for idx, score in enumerate(top_scores, 1):
        board.goto(0, y)
        board.write(f"{idx}. {score}", align="center", font=("Arial", 20, "normal"))
        y -= 32
    # Draw Try Again and Exit
    y -= 10
    board.goto(0, y)
    board.color("#00FF99")
    board.write("Press r to Try Again or Esc to Exit", align="center", font=("Arial", 16, "italic"))
    # Draw last score
    y -= 35
    board.goto(0, y)
    board.color("#CCCCCC")
    board.write(f"Your last score: {last_score}", align="center", font=("Arial", 15, "normal"))
    return board

def run_game(screen):
    screen.clear()
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    # Draw border
    border = turtle.Turtle()
    border.hideturtle()
    border.speed("fastest")
    border.color("white")
    border.penup()
    border.goto(-290, 200)
    border.pendown()
    for _ in range(2):
        border.forward(580)
        border.right(90)
        border.forward(400)
        border.right(90)
    border.penup()
    # Game objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 200 or snake.head.ycor() < -200:
            game_is_on = False
            scoreboard.game_over()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    return scoreboard.score

def main():
    last_score = 0
    while True:
        score = run_game(screen)
        save_score(score)
        board = show_scoreboard(screen, score)
        waiting = True
        def try_again():
            nonlocal waiting
            waiting = False
            board.clear()
        def exit_game():
            screen.bye()
        screen.onkey(try_again, "r")
        screen.onkey(exit_game, "Escape")
        while waiting:
            screen.update()
            time.sleep(0.1)

if __name__ == "__main__":
    main()