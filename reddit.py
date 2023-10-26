import os
import re
import praw
import markdown_to_text
import time
from videoscript import VideoScript

# Configuration variables
CLIENT_ID = "***************"
CLIENT_SECRET = "************************"
USER_AGENT = "Linux:SAED:1.0"
SUBREDDIT = "askreddit"

REDDIT_URL = "https://www.reddit.com/"


def getContent(outputDir, postOptionCount) -> VideoScript:
    reddit = __getReddit()
    existingPostIds = __getExistingPostIds(outputDir)

    now = int(time.time())
    autoSelect = postOptionCount == 0
    posts = []

    for submission in reddit.subreddit(SUBREDDIT).top(time_filter="day", limit=postOptionCount*3):  # month
        if (f"{submission.id}.mp4" in existingPostIds or post_in_file("posts.txt", submission.id)):  # or submission.over_18
            continue
        hoursAgoPosted = (now - submission.created_utc) / 3600
        print(f"[{len(posts)}] {submission.title}     {submission.score}    {'{:.1f}'.format(hoursAgoPosted)} hours ago")
        posts.append(submission)
        if (autoSelect or len(posts) >= postOptionCount):
            break
    if (autoSelect):
        return __getContentFromPost(posts[0])
    else:
        # postSelection = int(input("Input: "))
        postSelection = 0
        selectedPost = posts[postSelection]
        # print(selectedPost)
        return __getContentFromPost(selectedPost)


def getContentFromId(outputDir, submissionId) -> VideoScript:
    reddit = __getReddit()
    existingPostIds = __getExistingPostIds(outputDir)

    if (submissionId in existingPostIds):
        print("Video already exists!")
        exit()
    try:
        submission = reddit.submission(submissionId)
    except:
        print(f"Submission with id '{submissionId}' not found!")
        exit()
    return __getContentFromPost(submission)


def __getReddit():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )


def __getContentFromPost(submission) -> VideoScript:
    print(submission.url + " " + submission.title + " " + submission.id)
    content = VideoScript(submission.url, submission.title, submission.id)
    print(f"Creating video for post: {submission.title}")
    print(f"Url: {submission.url}")

    failedAttempts = 0

    for comment in submission.comments:
        if (content.addCommentScene(markdown_to_text.markdown_to_text(comment.body), comment.id)):
            failedAttempts += 1
        if (content.canQuickFinish() or (failedAttempts > 2 and content.canBeFinished())):
            break
        print(failedAttempts)
    return content


def __getExistingPostIds(outputDir):
    files = os.listdir(outputDir)
    files = [f for f in files if os.path.isfile(outputDir+'/'+f)]
    return [re.sub(r'.*?-', '', file) for file in files]


def post_in_file(file_name, target_word):
    with open(file_name, 'r') as file:
        content = file.read()

        words = content.split()

        if target_word in words:
            return True

    return False
