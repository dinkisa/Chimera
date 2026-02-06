# tests/test_skills_interface.py  
import pytest  
from skills.skill_download_youtube import download_youtube # Assuming your skill is in skills/skill_download_youtube.py  

def test_download_youtube_accepts_video_url():  
    try:  
        download_youtube(video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")  
    except TypeError as e:  
        pytest.fail(f"TypeError raised: {e}.  Skill likely doesn't accept the correct parameters.")  

# This test is designed to FAIL initially - you need to fill in the logic of download_youtube  
def test_download_youtube_actually_downloads_something():  
    with pytest.raises(NotImplementedError):  
        download_youtube(video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")  