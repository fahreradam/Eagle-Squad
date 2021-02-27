import pygame

class Variables:        #This is the pesky work-around to the "global variables" issue
    def __init__(self):
        #Main Menu Text
        self.font = pygame.font.SysFont("arial",45,bold=False,italic=False)     #Medium Font
        self.font2 = pygame.font.SysFont("arial", 60, bold=False, italic=False) #Large Font
        self.font3 = pygame.font.SysFont("arial", 30, bold=False, italic=False) #Small Font
        self.title_text = self.font2.render("LIBRARY HEIST", True, (255, 255, 255), None)
        self.play_text = self.font.render("START", True, (255, 0, 0), None)
        self.goals_text = self.font.render("GOALS", True, (255, 255, 0), None)
        self.credits_text = self.font.render("CREDITS", True, (0, 255, 0), None)
        self.exit_text = self.font.render("EXIT", True, (0, 0, 255), None)

        #Goals Screen Text
        self.goals_top_text = self.font3.render("These can be done in any order, but they must be completed BEFORE", True, (255, 255, 255), None)
        self.goals_top_text2 = self.font3.render("you can leave. Some of them require another to completed first.", True, (255, 255, 255), None)

        self.collect_books_goal_text = self.font3.render("#1: On 2 RANDOM Bookshelfs, there are 2 Books that you must collect.", True, (255, 255, 255), None)
        self.read_goal_text = self.font3.render("#2: Go to a TABLE and read one of the collected books.", True, (255, 255, 255), None)

        self.bathroom_goal_text = self.font3.render("#3: At a RANDOM point in the game, you will have to use the", True, (255, 255, 255), None)
        self.bathroom_goal_text2 = self.font3.render("Bathroom. You will be notified when this happens.", True, (255, 255, 255), None)

        self.power_goal_text = self.font3.render("#4: Somewhere there is a POWER Switch. Turning on Power", True, (255, 255, 255), None)
        self.power_goal_text2 = self.font3.render("Increases your Field of View and allows you to complete Goal #5.", True, (255, 255, 255), None)

        self.paper_goal_text = self.font3.render("#5: Find a COMPUTER for you to log into. This activates a PRINTER", True, (255, 255, 255), None)
        self.paper_goal_text2 = self.font3.render("With your piece of paper on it. Both of these are Random.", True, (255, 255, 255), None)

        self.secret_goal_text = self.font3.render("There is also a Hidden Puzzle, see if you can solve it!", True, (255, 255, 255), None)
        self.return_to_menu_text = self.font.render("RETURN", True, (255, 255, 255), None)

        #Credits Text Screen
        self.credits_top_text = self.font2.render("CREDITS:", True, (255, 255, 255), None)
        self.credit1 = self.font.render("Thomas Berryhill", True, (255, 255, 255), None)
        self.credit2 = self.font.render("Adam Fahrer", True, (255, 255, 255), None)
        self.credit3 = self.font.render("Miles McMurry", True, (255, 255, 255), None)
        self.credit4 = self.font.render("Jason Witherell", True, (255, 255, 255), None)
        self.credit5 = self.font.render("Clark Memorial Library", True, (255, 255, 255), None)
        self.credit6 = self.font.render("ID Software", True, (255, 255, 255), None)
        self.credit7 = self.font.render("Kenny's Assets", True, (255, 255, 255), None)
        self.credit8 = self.font.render("Shawnee State University", True, (255, 255, 255), None)

def draw_menu(win, V):
    win.fill((0,0,0))
    win.blit(V.title_text, (215, 50))
    win.blit(V.play_text, (350, 150))
    win.blit(V.goals_text, (345, 200))
    win.blit(V.credits_text, (325, 250))
    win.blit(V.exit_text, (370, 350))

def draw_goals_screen(win, V):
    win.fill((0, 0, 0))
    win.blit(V.goals_top_text, (10, 10))
    win.blit(V.goals_top_text2, (10, 40))
    win.blit(V.collect_books_goal_text, (10, 100))
    win.blit(V.read_goal_text, (10, 150))
    win.blit(V.bathroom_goal_text, (10, 200))
    win.blit(V.bathroom_goal_text2, (50, 230))
    win.blit(V.power_goal_text, (10, 300))
    win.blit(V.power_goal_text2, (52, 330))
    win.blit(V.paper_goal_text, (10, 400))
    win.blit(V.paper_goal_text2, (52, 430))
    win.blit(V.secret_goal_text, (10, 480))
    pygame.draw.rect(win, (0, 0, 255), (10, 530, 780, 50), 0)
    win.blit(V.return_to_menu_text, (325, 530))

def draw_credits_screen(win, V):
    win.fill((0, 0, 0))
    win.blit(V.credits_top_text, (290, 10))

    win.blit(V.credit1, (10, 100))
    win.blit(V.credit2, (10, 200))
    win.blit(V.credit3, (10, 300))
    win.blit(V.credit4, (10, 400))
    win.blit(V.credit5, (400, 100))
    win.blit(V.credit6, (400, 200))
    win.blit(V.credit7, (400, 300))
    win.blit(V.credit8, (350, 400))

    pygame.draw.rect(win, (0, 0, 255), (10, 530, 780, 50), 0)
    win.blit(V.return_to_menu_text, (325, 530))