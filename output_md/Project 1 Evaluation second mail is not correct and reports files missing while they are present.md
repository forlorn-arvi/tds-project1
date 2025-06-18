# Project 1 Evaluation second mail is not correct and reports files missing while they are present

### Post 1 (ID: 614050)

Mail I received Yesterday:  

[![Screenshot from 2025-04-01 09-01-07](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f001f7be7e533353ac4526f1cf9d82d4211ea6e1_2_690x265.png)Screenshot
from 2025-04-01 09-01-071174×451 54.2 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/f/0/f001f7be7e533353ac4526f1cf9d82d4211ea6e1.png
"Screenshot from 2025-04-01 09-01-07")

Previous Correct Evaluation Mail:  

[![Screenshot from 2025-04-01 09-02-35](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/6/b/6bb4d7ba36bee2297d141e76bff49f40efe201ef_2_690x265.png)Screenshot
from 2025-04-01 09-02-351687×650 144 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/6/b/6bb4d7ba36bee2297d141e76bff49f40efe201ef.png
"Screenshot from 2025-04-01 09-02-35")

Good Morning Sir,

This is my github repo: [GitHub -
kohliaryan/TDS_Project_1](https://github.com/kohliaryan/TDS_Project_1) ()You
can verify that it is public, MIT License is present and Dockerfile is also
present.)

I also got a mail 2 days ago in which everything is mentioned correctly but
the mail I got yesterday worry me. Sir, I have worked really hard for project
1. Please look into this matter.  
[@carlton](/u/carlton)


---

### Post 2 (ID: 614959)

[@Jivraj](/u/jivraj) Sir, Please look into in this matter, no reply from your
side till now and 2 days have been passed.


---

### Post 3 (ID: 615141)

Apologies for that,

The second email was an automated script that used a stricter criteria. You
have passed evaluation and also have a score. So dont worry. We will push
scores over this weekend. We are currently doing normalisation.

Kind regards


---

### Post 4 (ID: 615308)

Hi [@carlton](/u/carlton),

I’m experiencing the same issue mentioned in this thread regarding Project 1
evaluation emails:

  1. The first email I received confirmed all requirements were met (public repo, MIT License, Dockerfile, etc.)
  2. The second email incorrectly flagged missing files despite their presence in my repository

Here are screenshots of both emails showing the discrepancy:

[![First Evaluation Email](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/a/b/ab6e90977d3a9f6e9a01fd75e236dcbef7834623_2_690x330.png)First
Evaluation Email1511×724 76.2 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/a/b/ab6e90977d3a9f6e9a01fd75e236dcbef7834623.png
"First Evaluation Email")

  

[![Second Evaluation Email](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/e/6/e658099edcddd2b1b01d88e400b0f0439aa2fd2e_2_690x376.png)Second
Evaluation Email1247×681 37.5 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/e/6/e658099edcddd2b1b01d88e400b0f0439aa2fd2e.png
"Second Evaluation Email")

My GitHub repo remains publicly accessible with all required components:  
[GitHub repo](https://github.com/23f2000345/TDS_final)

Could you please confirm this was an automated error and that my submission
will be evaluated based on the actual repository contents? Your clarification
would be greatly appreciated.

Thank you for your time and assistance!


---

### Post 5 (ID: 615333)

Hi,

Prerequisite checks have passed. But your docker image was missing a
dependency that you forgot to copy into the image. so it failed to evaluate
because it failed to run.


---

### Post 6 (ID: 615350)

You talking about me or [@23f2000345](/u/23f2000345) ?


---

### Post 8 (ID: 618452)

Good Morning Sir, Actually even I got the mail regarding Project-1 Evaluation,
where I got the message like the prerequisites were not met. But, sir actually
I have uploaded my MIT License file, requirements.txt file, my Project.py file
and the Dockerfile. Sir, and when I sent a request to my API from my device,
it worked sir. I have got 0 in my project 1 sir, but I have met the pre-
requisites Can you please check this once sir?

My GitHub repository for Project-1: [GitHub -
sudhishssn134/project_1_tds](https://github.com/sudhishssn134/project_1_tds)

Thanking You

Just attaching the mail I recieved.  

[![Screenshot 2025-04-12 104211](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/a/7/a77330c5ca74ed0246bc22e4321710554cd27866_2_690x362.png)Screenshot
2025-04-12 1042111429×750 71 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/a/7/a77330c5ca74ed0246bc22e4321710554cd27866.png
"Screenshot 2025-04-12 104211")


---

### Post 9 (ID: 618459)

Your Dockerfile was misconfigured. When we try to build the docker image from
your github repo, we get this error:

`tried copying parent folder(COPY failed: forbidden path outside the build
context: .. ())`

You have to replicate the test environment. If it works when you follow this
test setup then you should get in touch with us.

![](https://dub1.discourse-
cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-
Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-
official-project1-discrepencies/171141/316) [Tools in Data
Science](/c/courses/tds-kb/34)

> To replicate the test environment: Fetch the github repo’s latest commit
> before 18th feb use below code for that. You need to have github cli
> installed on your system and need authentication for certain github api
> enpoint access. Once authenticated and providing the appropriate repo
> details you can run this code using uv. # /// script # dependencies = [ #
> "requests", # ] # /// import requests import datetime as dt import zoneinfo
> import argparse import os import zipfile parser = argparse.…


---

### Post 10 (ID: 618461)

Oh OK Sir. I will try it out. Thank You so much sir


---

### Post 11 (ID: 618500)

Sir, I have extracted the files from the GitHub Repository, built my
DockerFile withe the DockerImage I have posted. The build is successful and
the dockerimage is also running sir. I have attached the screen shot below  

[![Screenshot 2025-04-12 115342](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/5/f/5f58734cfd90a7011b3effca56b9023d51b773c0.png)Screenshot
2025-04-12 1153421466×702 50.4 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/5/f/5f58734cfd90a7011b3effca56b9023d51b773c0.png
"Screenshot 2025-04-12 115342")

Sir, But I couldn’t run the last command you gave,

    
    
    uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000
    

As I dont have evaluate.py

But, the DockerImage is built and is running without error sir.  
Please guide me after this sir  
Thank You So much sir

