import string
import pyperclip
import pygame
import pygame_gui
import random as rand


def Generate(n, password):
    password.append(''.join([rand.choice(
        string.ascii_letters + string.digits)
        for i in range(n)]))


pygame.init()


def main():

    IsGenerated = False

    n = 0

    Letters = []

    Letters.append(string.ascii_letters)
    Letters.append(string.punctuation)
    Letters.append(string.digits)

    password = []

    pygame.display.set_caption('Password Generator')
    window_surface = pygame.display.set_mode((1024, 768))

    background = pygame.Surface((1024, 768))
    background.fill(pygame.Color('#57555D'))

    manager = pygame_gui.UIManager((1024, 768))

    Password_Btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((380, 450), (256, 50)),
                                                text='Generate Password',
                                                manager=manager)
    Password_Lngth = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((250, 360), (512, 50)),
                                                         manager=manager)
    Result = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((250, 405), (512, 50)), html_text="Result: ",
                                           manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and IsGenerated:
                if event.ui_element == Password_Lngth:
                    password.clear()
                    password = []

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == Password_Btn:
                    Generate(int(Password_Lngth.get_text()), password)
                    password = str(password).replace("'", '')
                    password = password.replace('[', '')
                    password = password.replace(']', '')
                    Result.append_html_text(password)
                    pyperclip.copy(password)
                    IsGenerated = True


            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


if __name__ == '__main__':
    main()
