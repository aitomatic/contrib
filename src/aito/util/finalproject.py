import pygame
import random
import time
import turtle
# Class thể hiện đối tượng Câu hỏi
# Một đối tượng Question gồm có 2 fields: 
# - question: đề bài
# - answer: đáp án
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

        
# Class thể hiện trạng thái hiện tại của trò chơi
class GameState:
    # Điểm số hiện tại
    score = 0
    roundnum = 1
    # Khởi động lại đồng hồ bấm giờ: cho giá trị bằng thời gian hiện tại
    def reset_timer(self):
        self.start_time = time.time()
    # Trả về thời gian trả lời câu hỏi (tính bằng giây), bằng cách lấy
    # thời gian đồng hồ trừ đi thời gian start_time đã lưu.
    def get_timer(self):
        return time.time() - self.start_time

# Khởi tạo đối tượng cụ thể lưu trạng thái của trò chơi
state = GameState()

# Dùng thư viện pygame để chơi âm thanh. 
def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
def play_sound(file):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
# Vẽ hình nhân vật.
avatar = turtle.Turtle()         
def draw_avatar(image):
    # Phải gọi lệnh turtle.addshape trước khi vẽ ảnh.
    turtle.addshape(image)  
    avatar.clear()
    avatar.penup()
    avatar.setposition(350, -100)
    # Lưu ý: turtle chỉ vẽ được ảnh có định dạng .gif
    avatar.shape(image)

# Khởi tạo cây bút chuyên dùng để vẽ thời gian.
pen_timer = turtle.Turtle()
def draw_timer():
    # Ẩn con rùa.
    pen_timer.hideturtle()
    # Nhấc bút lên.
    pen_timer.penup()
    # Xoá, để khi vẽ điểm không bị đè lên nhau.
    pen_timer.clear()
    # Đổi màu.
    pen_timer.color('green')
    # Đặt vị trí.
    pen_timer.setposition(-240, 170)
    # Viết điểm số ra màn hình.
    pen_timer.write(round(state.get_timer()), font=get_font(20))
    # Vẽ lại điểm số sau 1000ms (1 giây) nữa
    turtle.Screen().ontimer(draw_timer, 1000)
# Khai báo dữ liệu câu hỏi và đáp án
def read_data(round_num):
    # Đọc câu hỏi và đáp án từ Files.
    # Số lượng câu hỏi
    num_questions = 3
    # Ban đầu, mảng dữ liệu là trống
    data = []
    # Các file câu hỏi đánh số là q1.txt, q2.txt, q3.txt,...
    # Các file câu trả lời đánh số là a1.txt, a2.txt, a3.txt,...
    # Ta dùng hàm range(1, x + 1) để duyệt qua các số 1, 2, ..., x
    for i in range(1, num_questions + 1):
        # Đọc câu hỏi, dùng encoding='utf-8' để đọc tiếng Việt
        filename ='r' + str(round_num) + 'q' + str(i) + '.txt'
        f = open(filename, 'r', encoding='utf-8')
        question = f.read()
        f.close()    
        
        # Đọc đáp án
        filename ='r' +str(round_num) + 'a' + str(i) + '.txt'
        f = open(filename, 'r', encoding='utf-8')
        answer = f.read()
        f.close()    

        # Tạo đối tượng Question và thêm vào mảng dữ liệu data
        data.append(Question(question, answer))
    # Trả về mảng dữ liệu data     
    return data


# Sinh ra các câu hỏi tính nhẩm ngẫu nhiên Siêu Trí Tuệ
def generate_math_questions(round_num):
    # Ban đầu, danh sách câu hỏi trống.
    data = []
    # Số lượng câu hỏi sinh ra.
    num_questions = 3
    # Hai phép toán: cộng và nhân
    operators = ["+", "x"]    
    # Số lượng chữ số tối đa khi sinh câu hỏi ngẫu nhiên
    
    if round_num == 1:
        max_digits = 9
        min_digits = 1
    elif round_num == 2:
        max_digits = 99
        min_digits = 10
    else:
        max_digits = 999
        min_digits = 100
    for i in range(num_questions):
        # Chọn số ngẫu nhiên từ 0 đến 10^max_digits - 1
        a = random.randint(min_digits, max_digits)
        b = random.randint(min_digits, max_digits)
        # Chọn một phép toán ngẫu nhiên
        op = random.choice(operators)
        # Sinh ra đề bài
        question = str(a) + " " + op + " " + str(b) + " = ?"
        # Sinh ra đáp án
        if op == "+":
            answer = a + b
        elif op == "x":
            answer = a * b            
        # Thêm câu hỏi vào danh sách
        data.append(Question(question, str(answer)))
    # Trả về danh sách câu hỏi tính nhẩm Siêu Trí Tuệ.
    return data


# Trả về font chữ với kích thước được cho.
def get_font(font_size):
    return ("Arial", font_size, "normal")

# Khởi tạo cây bút chuyên dùng để vẽ Điểm số.
pen_score = turtle.Turtle()
def draw_score():
    # Ẩn con rùa.
    pen_score.hideturtle()
    # Nhấc bút lên.
    pen_score.penup()
    
    pen_score.clear()
    
    
    pen_score.color('red')
    
    pen_score.setposition(300, 175)
    
    temp ="ROUND: "+ str(state.roundnum)
    pen_score.write(temp, font=get_font(30))
    
    pen_score.color('white')
    
    pen_score.setposition(340, 110)
    
    pen_score.write(state.score, font=get_font(40))

pen_round = turtle.Turtle()
def draw_round_number(round_num):
    pen_round.hideturtle()
    
    pen_round.penup()
    
    pen_round.clear()
    
    pen_round.color('red')
    
    pen_round.setposition(300, 175)
    
    temp ="ROUND: "+ str(state.roundnum)
    pen_round.write(temp, font=get_font(30))


def ask_question(question):
    
    print("***************************")
    print(question.question)
    
    turtle.clear()
     
    turtle.hideturtle()
    
    turtle.penup()
    
    turtle.setposition(-240, 20)
    
    turtle.write(question.question, font=get_font(15))
    
    draw_score()
     
    draw_avatar('KimNguu-normal.gif')
    
    state.reset_timer()

    result = turtle.textinput("Siêu Lập Trình", "Câu trả lời của bạn là gì?\n")
    
    check_result(result, question.answer)
    
def check_result(result, answer):

    time_taken = state.get_timer()
    
    if time_taken < 5:
        bonus = 5
    else:
        bonus = 0
    state.roundnum =round_number
    if result == answer:
         
        state.score += 10 + bonus
        
        play_sound("correct_answer.wav")

        draw_avatar('KimNguu-correct.gif')
        print("Đúng rồi")
    else:
         
        play_sound("wrong_answer.wav")

        
        draw_avatar('KimNguu-wrong.gif')
        print("Sai rồi")

    time.sleep(0.5)
    print("Thời gian trả lời câu hỏi là:", round(time_taken), "giây")
    if bonus > 0:
        print("Bạn nhận được điểm thưởng là", bonus, "vì trả lời nhanh")            
    print("Điểm hiện tại của bạn là: ", state.score)

def setup_turtle():
    
    screen = turtle.Screen()
    
    screen.setup(1200, 600)
    
    screen.bgpic('background.gif')
    
    turtle.title("Siêu lập trình")
    
# Gọi hàm thiết lập màn hình    
setup_turtle()
# Chơi nhạc
play_music("music.wav")

# Vẽ thời gian
state.reset_timer()
draw_timer()

round_number = 1
while round_number < 4:
    #draw_round_number(round_number)    
    data = read_data(round_number) + generate_math_questions(round_number)
    for question in data:
        ask_question(question)
    round_number += 1
