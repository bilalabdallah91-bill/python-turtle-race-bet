import random
import turtle

# 1. إعداد الشاشة ونافذة التخمين
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race - سباق السلاحف")

# ألوان السلاحف المشاركة
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# طلب تخمين المستخدم عبر نافذة رسومية
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

# 2. إنشاء السلاحف وتحديد أماكن البداية
for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# 3. بدء السباق إذا قام المستخدم بإدخال لون
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_item in all_turtles:
        # خط النهاية عند X = 230
        if turtle_item.xcor() > 230:
            is_race_on = False
            winning_color = turtle_item.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!"
                )

        # تحريك السلحفاة بمسافة عشوائية
        random_distance = random.randint(0, 10)
        turtle_item.forward(random_distance)

screen.exitonclick()
