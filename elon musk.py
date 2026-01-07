# මෙය ගේම් ලූප් එක (While loop) ඇතුළත drawing කොටසට එකතු කරන්න

def display_message():
    # පණිවිඩය පෙන්වන කොටුව (Dialogue Box)
    box_rect = pygame.Rect(50, 450, 700, 100)
    pygame.draw.rect(screen, (0, 0, 40), box_rect) # තද නිල් පාට පෙට්ටිය
    pygame.draw.rect(screen, (0, 255, 255), box_rect, 2) # වටේට ලස්සන බෝඩර් එකක්
    
    # පණිවිඩය ලියමු
    msg_font = pygame.font.SysFont("Arial", 28, bold=True)
    text_surface = msg_font.render("Mission Control: Elon, I wish you a safe journey, Hero!", True, (255, 255, 255))
    screen.blit(text_surface, (70, 485))

# ගේම් එක පටන් අරන් ටික වෙලාවක් යනකම් මේක පෙන්නන්න
if score < 300: 
    display_message()
