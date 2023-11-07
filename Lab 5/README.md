# Observant Systems

**NAMES OF COLLABORATORS HERE**: Carlos Suberviola, Neelraj Patil, Ivan Nikitovic

ChatGPT was used to choose random milestone images and assign them to an emotion. It was also used for uplifting messages. 
```
mood_to_images = {
    "happy": [
        "mewithfriends.jpg",  # Social gatherings often boost happiness.
        "puppy.jpg",          # Cute animals are a common source of joy.
        "graduation.jpg",     # Celebrating personal achievements can make someone happy.
        "birthday_party.jpg", # Birthday celebrations are typically joyous occasions.
        "concert_night.jpg",  # Music events are often associated with happiness and excitement.
        "baby_steps.jpg",     # Family milestones like a baby's first steps bring happiness.
    ],
    "sad": [
        # Typically, one does not seek to view images to enhance sadness, but certain images might offer comfort during sadness.
        "puppy.jpg",          # Pets can provide comfort during sad times.
        "first_day_school.jpg", # Parents might feel a bittersweet sadness seeing children grow up.
        "snowman_winter.jpg", # Seasonal activities might remind someone of happier times.
    ],
    "angry": [
        "workout.jpg",        # Physical activity is often sought to channel and alleviate anger.
        "hiking_trails.jpg",  # Engaging with nature can be calming when angry.
    ],
    "stressed": [
        "beach_sunset.jpg",   # Natural scenery, like a beach at sunset, can be calming for stressed individuals.
        "home_cooked_meal.jpg", # Comfort food, or the act of cooking, can be stress-relieving.
        "snowman_winter.jpg", # Creative activities like making a snowman can distract and reduce stress.
    ],
}
```
```
mood_messages = {
    "happy": [
        "Keep riding that wave of joy—it's great to see you so upbeat!",
        "Your happiness is contagious! Keep spreading that positive energy around you!",
        "It's wonderful to see you so happy! Keep enjoying every moment to the fullest!",
    ],
    "sad": [
        "Even on a cloudy day, the sun is still shining. Hang in there, and you'll see it soon!",
        "It's okay to feel down—remember, every storm passes and leaves a clear sky.",
        "Sending you a little box of sunshine to brighten your day as you always brighten mine!",
    ],
    "angry": [
        "Take a deep breath and feel the peace flowing in. You've got this!",
        "It's absolutely okay to feel angry, but remember to give yourself the gift of calmness soon.",
        "Imagine your anger as a balloon. Now let it go and watch it disappear into the sky.",
    ],
    "stressed": [
        "Remember to take things one step at a time—you're doing way better than you think!",
        "Deep breaths. You're stronger than your stress. You can conquer anything!",
        "Stress is just the weight of things that matter. Let's find a way to lighten your load."
    ]
}

```

### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.


**Describe and detail the interaction, as well as your experimentation here:**  
We wanted to try to construct an interaction with facial expressions, such that the Raspberry Pi would predict an emotion based off of a user's face. We tried a few libraries to accomplish this task of recognition, such as Teachable Machines (which didn't work well) and DeepFace (worked very well). We tried basic emotions, like happy, sad, angry, and stressed (coded as fear). DeepFace also supported a neutral facial expression and a few others as well. We each tried to use the model and had similar positive results. We also tried to confuse the model with having two faces present, but it correctly detected both faces. We did not implement anything for dealing with more than one face, but it appears that the model would support it. Based on this result, we wanted to create a tool to improve/maintain one's mood through smart devices in their home. We created a handler for four selected emotions (happy, sad, angry, and fearful) that would attempt to cheer the user up or maintain their happiness. Our application pulls from a pseudo-Instagram library of images (Ideally we would actually link to a user's instagram account) and, when a certain emotion is detected, that picture is printed along with its caption, tagged friends, and date. For example, a sad user could have a photo of their dog automatically chosen and printed, as pets often cheer people up. Also, our program would use a text to speech engine to say an uplifting phrase in an attempt to cheer the user up. 

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:

1. When does it what it is supposed to do?

When a user's emotion is correctly identified and an image/spoken message are chosen such that they cheer the user up or maintain their feelings of happiness. For example, I acted sad and was printed a picture of my dog and told that it's okay to feel sad.  
1. When does it fail?

When a user's emotion is not correctly identified or the image/spoken message that are chosen do not cheer the user up or maintain their happiness. For example, if I act angry and am printed a picture of a friend with whom I am in an argument, that would perpetuate my anger. 
1. When it fails, why does it fail?

The failure could be caused by the AI tool misclassifying my facial expression or by misassociating pictures/phrases with improving a certain mood. 
1. Based on the behavior you have seen, what other scenarios could cause problems?

The printing process can sometimes take multiple minutes to execute, meaning there is an awkward delay between showing signs of an emotion and actually receiving the printed response. Alternatively, the user may not want to be consoled or watched when they are experiencing emotional distress. 

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?

Users should ideally be made aware of the uncertainties in the system. They should understand that emotion recognition is not infallible, and there might be occasional misclassifications. This awareness can help manage expectations and reduce the impact of misclassifications.

2. How bad would they be impacted by a miss classification?

The impact of a misclassification depends on the individual and the context. For some users, a misclassification might be inconsequential, while for others, it could be distressing. Misclassifying negative emotions as positive or vice versa could potentially worsen the user's mood or cause discomfort.

3. How could change your interactive system to address this?

To address misclassifications, the system can be improved through user feedback, personalization, contextual understanding, and threshold setting. User feedback allows for the correction of emotion classifications to enhance system accuracy. Personalization involves creating user profiles to tailor responses to individual preferences. Contextual understanding enhances the algorithm's ability to consider context, prioritizing content based on a user's known preferences. Threshold setting empowers users to define content sensitivity levels, enabling the system to adjust responses accordingly.

4. Are there optimizations you can try to do on your sense-making algorithm?

The optimization of the sense-making algorithm involves several strategies. It includes ongoing machine learning refinement through diverse dataset training to enhance accuracy and minimize misclassifications. Feature engineering explores additional cues like voice tone, body language, and contextual information from previous interactions for improved emotion recognition. The utilization of ensemble models combines multiple emotion recognition outputs to bolster predictions, and a real-time feedback loop continuously learns from user feedback, fine-tuning the model's predictions in response.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use MoodHelper for?

You can use MoodHelper for identifying and responding to users' emotions. It can select appropriate content, such as images and spoken messages, to either uplift or maintain the user's emotional state based on real-time emotion recognition.

* What is a good environment for MoodHelper?

A good environment for MoodHelper is one where there is adequate lighting and visibility of the user's face for accurate facial expression analysis. It thrives in environments with clear audio for spoken messages to be heard and benefits from a reliable internet connection for quick content retrieval.

* What is a bad environment for MoodHelper?

A bad environment for MoodHelper includes situations where the user's face is poorly illuminated, making facial expression recognition challenging. It struggles in noisy environments where spoken messages can not be clearly understood. Additionally, slow or unreliable internet connections hinder the prompt delivery of content.

* When will MoodHelper break?

MoodHelper is more likely to break when it encounters extreme or mixed emotions that are challenging to classify accurately. It may also break when the user's face is obscured or not visible due to factors like low lighting or camera positioning.

* When it breaks how will MoodHelper break?

When MoodHelper breaks, it may provide incorrect content in response to the user's emotions, potentially aggravating their mood instead of improving it. For instance, it may offer inappropriate images or messages that do not align with the user's actual emotional state.

* What are other properties/behaviors of MoodHelper?

MoodHelper has the property of adaptability, as it could be improved to learn from user feedback to improve emotion recognition and response accuracy over time (currently wizarded). It could exhibit the behavior of personalization by tailoring responses based on a user's historical interactions and preferences.

* How does MoodHelper feel?

MoodHelper, being an AI-based system, doesn't have feelings in the human sense, so it uses its camera to read facial expressions. It is designed to enhance and manage the emotional experience of users, aiming to provide comfort or upliftment when users are in need.


**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***
[Video Answering Questions with Mini Demo](https://drive.google.com/file/d/1vpadU-BWhfzkQde2N2f5w6BTTmAoCCBW/view?usp=sharing)

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
