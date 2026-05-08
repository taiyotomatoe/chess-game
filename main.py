# import pygame

# screen_size = 720
# pygame.init()
# screen = pygame.display.set_mode((screen_size, screen_size))
# clock = pygame.time.Clock()
# running = True

# def draw_board(): 
#     pygame.draw.rect(screen, color=(255,0,0), rect=[600,100,100,100])

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill("blue")

#     draw_board()

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     clock.tick(60)  # limits FPS to 60

# pygame.quit()

    

class black_piece: 
    pieces_remaining = 16
    def __init__(self, piece, position):
        self.position = position
        self.piece = piece
    
    def move(self, move_for): 
        if self.piece == "Pawn": 
            self.position = self.position =+ move_for

pawn_1 = black_piece("Pawn", 0)
print(pawn_1.position)

first.move(1)   
print(pawn_1.position)

