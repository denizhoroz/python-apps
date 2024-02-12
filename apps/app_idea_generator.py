import random as r
import os

businesses = ['health', 'education', 'finance', 'travel', 'design', 'retail', 'service', 'engineering', 'entertainment', 'news', 'food', 'social', 'security']
aud_age = ['everyone', 'children', 'teenagers', 'young adults', 'adults', 'senior citizens']
aud_design = ['artists', 'writers', 'musicians', 'designers', 'filmmakers', 'game developers']

categories = ['manager', 'cleaner', 'generator', 'converter', 'planner/tracker', 'informative', 'games']
platform = ['mobile', 'desktop', 'web']

def generate_idea():
    sel_bus = r.choice(businesses)
    sel_cat = r.choice(categories)
    sel_plat = r.choice(platform)
    
    
    if sel_bus == 'engineering':
        audience = 'engineers'
    elif sel_bus == 'design':
        audience = r.choice(aud_design)
    else:
        audience = r.choice(aud_age)

    result = f'A/An {sel_bus} {sel_cat} app on {sel_plat} platforms, for {audience}'
    return result

idea_prompt = generate_idea()

print(f'New Idea:\n{idea_prompt}')

