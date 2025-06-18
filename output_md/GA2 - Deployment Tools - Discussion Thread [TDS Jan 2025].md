# GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]

### Post 1 (ID: 575521)

Please post any questions related to [Graded Assignment 2 - Deployment
Tools](https://exam.sanand.workers.dev/tds-2025-01-ga2).

* * *

## Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through [Discourse Docs](/c/docs-
discourse/45)! ![:slight_smile:](https://emoji.discourse-
cdn.com/google/slight_smile.png?v=12)

* * *

Deadline: Sunday, February 2, 2025 6:29 PM

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


---

### Post 2 (ID: 576110)




---

### Post 4 (ID: 579138)

[![Screenshot 2025-01-12 223630](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/f/2/f2485af8a009f815219a3df4bbdf15db1322608e_2_690x77.png)Screenshot
2025-01-12 2236301727×195 27.1 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/f/2/f2485af8a009f815219a3df4bbdf15db1322608e.png
"Screenshot 2025-01-12 223630")

  
i have included the email address still its giving error


---

### Post 5 (ID: 578933)

[![Screenshot 2025-01-12 223956](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/e/f/ef0c6289076549898612976667c10de3886cc953_2_690x65.png)Screenshot
2025-01-12 2239561674×158 12.8 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/e/f/ef0c6289076549898612976667c10de3886cc953.png
"Screenshot 2025-01-12 223956")

  
that website is working fine . just write the parameters after /api


---

### Post 6 (ID: 578996)

Hi Guddu,

Can you share your GitHub repo. For GitHub pages question.


---

### Post 7 (ID: 578997)

Check your browser console most probably CORS is causing problem.

Try adding CORS to your code it might work.

Kind regards  
Jivraj


---

### Post 8 (ID: 579058)

[github.com](https://github.com/gkmfrombs/dolfacts)

![](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b67fc201449a012745d92b7efdcf9e92fc7a35b_2_690x344.png)

### [GitHub - gkmfrombs/dolfacts](https://github.com/gkmfrombs/dolfacts)

Contribute to gkmfrombs/dolfacts development by creating an account on GitHub.

I have added email in body two times in different ways.


---

### Post 9 (ID: 579445)

[![Screenshot 2025-01-14 at 1.39.39 AM](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/2/4/243cab0b6d8a65099dfe8b13b242dd816a4f3205_2_690x431.jpeg)Screenshot
2025-01-14 at 1.39.39 AM1440×900 154 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/2/4/243cab0b6d8a65099dfe8b13b242dd816a4f3205.jpeg
"Screenshot 2025-01-14 at 1.39.39 AM")

  
[@carlton](/u/carlton) can you please tell me what is wrong in this because I
am getting “Error: Response undefined does not match expected” to my answer


---

### Post 10 (ID: 579556)

Facing Issue in GA 2 Question 10 LLM ngrok  

[![image](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/e/2/e2d34a628bc87d88e8e28cbb9a08254c16f6ba76_2_690x318.png)image1920×886
45.7 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/e/2/e2d34a628bc87d88e8e28cbb9a08254c16f6ba76.png
"image")

  
I tired multiple times but issue is still there.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) Kindly help
me out.


---

### Post 11 (ID: 579564)

Hi Mishkat,

Please use triple backticks to encapsulate code, so that we can debug your
code more easily.

eg

    
    
    if __name__ == "__main__":
       print ("Hello")
    

Please use this discourse etiquette to share code.

Thanks and kind regards


---

### Post 12 (ID: 579571)

sir did you check yet what is the problem in this one?


---

### Post 13 (ID: 579593)


    from fastapi import FastAPI, Query
    from fastapi.middleware.cors import CORSMiddleware
    from typing import List, Optional
    import csv
    
    app = FastAPI()
    
    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allow all methods
        allow_headers=["*"],  # Allow all headers
    )
    
    # Load student data from the specified CSV file
    students = []
    with open('/Users/mish/Downloads/q-fastapi.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "studentId": int(row["studentId"]),
                "class": row["class"]
            })
    
    @app.get("/api")
    async def get_students(class_: Optional[List[str]] = Query(None)):
        print(f"Requested classes: {class_}")  # Debugging line
        if class_:
            filtered_students = [student for student in students if student["class"] in class_]
            print(f"Filtered students: {filtered_students}")  # Debugging line
            return {"students": filtered_students}
        return {"students": students}
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
    


---

### Post 14 (ID: 579600)

Hi Mishkat,

This error is because you are filtering on `class_` instead of `class`

So if you send a request on `http://127.0.0.1/api?class_=1S` you will see
response for that `1S` class only.

kind regards


---

### Post 15 (ID: 579603)

thank you so much after modifying the code it got accepted


---

### Post 16 (ID: 579617)

Hi Guddu,

Inside `index.html` file of your repo, don’t put html code just put your email
in the file nothing else.

This issue is because when you deploy on github pages it encrypts any email
that’s on page.

kind regards.


---

### Post 17 (ID: 579621)

I am facing an issue with Docker Desktop.

[![Docker Desktop Error](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/d/7/d7bcf7a2f709561b98fa8bde031ab5d1e81a4a0d.png)Docker
Desktop Error558×377 27 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/d/7/d7bcf7a2f709561b98fa8bde031ab5d1e81a4a0d.png
"Docker Desktop Error")

I have uninstalled and installed Docker (run as administrator).

wsl --version

    
    
    WSL version: 2.3.26.0
    Kernel version: 5.15.167.4-1
    WSLg version: 1.0.65
    MSRDC version: 1.2.5620
    Direct3D version: 1.611.1-81528511
    DXCore version: 10.0.26100.1-240331-1435.ge-release
    Windows version: 10.0.19045.5011
    

Tried many solutions after googling for the issue.  
So far no solution. Anyone else faced this issue and found a solution?


---

### Post 18 (ID: 579625)

Hi Telvin,

Try opening `localhost:8080` in browser if that works, if it opens in browser
then issue might be with some network configurations.

I solved this question in github codespace, which didn’t require me to make
any changes in network.

kind regards

kind regards


---

### Post 19 (ID: 579634)

[@Nelson](/u/nelson) I would recommend [Podman](https://podman.io/) or [Docker
CE](https://docs.docker.com/engine/install/ubuntu/) rather than [Docker
Desktop](https://www.docker.com/products/docker-desktop/).

Docker Desktop is [not free for organizations over 250
people](https://docs.docker.com/subscription/desktop-license/) and many
organizations have therefore moved away from it.


---

### Post 20 (ID: 579653)

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) I tired ,
in browser localhost:8080 is working fine but ngrok is not working. Is there
any other tools for tunneling that can be used.


---

### Post 21 (ID: 579662)

[@22f2001640](/u/22f2001640) in that case

  * a firewall or local security settings might block access to port 8080, or
  * a network restriction is blocking access to port 8080

Please try one of these:

  * Try the same on a personal laptop on a public / home network
  * GitHub codespaces, as [@Jivraj](/u/jivraj) suggested

You _could_ try an ngrok alternative like
[localtunnel](https://localtunnel.github.io/www/) but I don’t think that’ll
work.

