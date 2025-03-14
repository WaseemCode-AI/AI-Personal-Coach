def track_progress(user_goal, progress_level):
    motivation_quotes = [
        "Mehnat ka fal meetha hota hai!",
        "Har din ek naye chance ki shuruaat hai!",
        "Tum apne sapne jee sakte ho, bas lagatar mehnat karo!"
    ]
    
    if progress_level < 30:
        return "Shuruaat acchi hui hai, aur mehnat karo! " + motivation_quotes[0]
    elif progress_level < 70:
        return "Aage badh rahe ho, continue rakho! " + motivation_quotes[1]
    else:
        return "Tum apne goal ke bohot kareeb ho, bas ek push aur! " + motivation_quotes[2]

if __name__ == "__main__":
    goal = "Fitness"
    progress = 50
    print(track_progress(goal, progress))
