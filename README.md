# Freely - A Chatapp built on Web3
### Video Demo: https://youtu.be/Mz1TT9GQ9CQ
### Description:

Welcome to Freely - a Web3 application that enables decentralization in a simple chat app! The webapp was written in Python (Flask), JavaScript, HTML and CSS.

Features:
- Fully decentralized: With the use of SocketIO, you can still chat asynchronously without sacrificing privacy. The chat app was serverless so no one can read your messages!
- Metamask authentication: Simply connect your wallet that holds our [Edition-drop NFT](https://portal.thirdweb.com/pre-built-contracts/edition) and enter your username of choice, you are in!
- NFT integration: I strongly believe that NFTs are more than apes and PNGs, they are the future of identity and validation! 
- Modern design: I leverage the use of [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/). 
-  Animation: With two simple library ([animate css](animate.css) and [animate on scroll](https://michalsnik.github.io/aos/)), the website appears more lively and user-friendly.

Requirements:
Can be found in requirements.txt

Functions Flow chart:
![Flowchart](https://i.ibb.co/2KdKQ7D/Screenshot-2022-08-20-110120.png)

### Components of the project:
*layout.html*

The file is the backbone of the project and was used on every site. It consisted of 3 main parts: the Navigation bar, the main body and the footer. 
- The Navigation bar: integrates [Scrollspy](https://getbootstrap.com/docs/5.2/components/scrollspy/) from Bootstrap with smooth scrolling enabled.
- Main body: left blank for templating.
- Footer: Small muted text that sticks to the bottom with `class="fixed-bottom"`


*index.html*

Consisted of 2 sections: the main landing page and the instructions, separated by a lightweight divider. 
- Landing page: animated text components, small button to proceed to authentication page.
- Instructions: used Animation On Scroll Library, simple fade-in animation when users reached the section.

*connect.html*

Simple card with Metamask logo and Connect button.  Automatically prompting users to connect their wallet with `window.addEventListener('DOMContentLoaded')`
Submit a form to app.py for NFT balance validation:
- User has not installed Metamask: Card updates with guides to install Metamask extension.
- User has installed Metamask but has NOT minted the NFT: Redirect user to *mint.html*.
- User has installed Metamask and has minted the NFT: Prompting a username of choice and continue to the chatroom.

*mint.html*

Simple widget embedded on the page from ThirdWeb. The page then handles Wallet connection and gasless minting.
**NFT**: Non-fungible Token
**Edition-drop NFT**: One NFT, multiple owners. [The Pioneer NFT](https://thirdweb.com/mumbai/edition-drop/0xdc024d592D197053BdEcB966121C323A846EF1a5?tabIndex=0) acts as a pass to access content on the webpage. 
**Mumbai Testnet**: [A Testnet on Polygon Network](https://docs.polygon.technology/docs/develop/network-details/network/). Fast transactions with little to no gas fee, uses MATIC token. 
**Gasless minting**: I followed ThirdWeb documentation and set up a Relayer with an automated task to pay the gas fee for the minting process on [OpenZepplin Defender](https://www.openzeppelin.com/defender). Users can now mint the NFT without the need to pay any fees.

*exclusive.html* 

The main chatapp lies here on this html. I used SocketIO for real-time polling data and Flask-SocketIO for Python Flask compatibility. I followed Code Penguin's tutorial to achieve the complete application. Now users can chat asynchronously when connected to the chat room.

SocketIO pros and cons:
|Pros|Cons  |
|--|--|
|Severless|No chat history|
|Decentralized|Outdated|
|Simple to deploy |Unsecured|


### Problems and Solutions:
During the initial making of the project, I faced a lot of hardships and here are some of them:
- Technology: powerful webapp are built on JavaScript and its vast amount of frameworks but I decided to stick with Python and Flask. As a result, the resources are not abundant.
- Time constraint: with only 7 days to fully engineered a webapp and deploy it for mass users integration, I found it really stressful to think about the deadline sometimes.
- Design of the website: yep the hardest part of building a website was actually how to convert sketches on Figma into HTML codes (especially with spacing and sizing elements) 75% of the time I spent on this project was for tweaking with different variables and layouts.
- Asynchronous coding: I had little to zero knowledge about WebSockets and Polling in data communication between the server and the client, so debugging took quite a while. The SocketIO tutorial by Code Penguins was quickly outdated (despite being released in late 2020) which led to countless hour trying different package versions and tweaking virtual environment.
- Heroku deployment: This is by far the most frustrating part. Although I was quite familiar with Git in project development, Heroku was still something really confusing. I was faced by multiple `failed to push some refs to https://myproject.herokuapp.com`, countless 400 Bad Requests (different server configuration when migrating from localhost:5000). Slight tweak, commit, push and debug.

After all, I have found some of the most valuable lessons after the project, as well as helpful advice for my future self:
- Make sure to understand the code before merging it into my project. 3 hours of searching far and wide just to find out I forgot to change the server protocol from the example.
- Google really was my BEST friend. 
- Break things down into small, consumable pieces instead of trying to digest everything at once. Well, Heroku was not as confusing as I thought, I just committed into the wrong branch :D
- `python -m venv venv` came in clutch! Sometimes. `git reset -- venv` to avoid committing 5000 files of virtual environment components onto your GitHub. 
- GitHub has changed its main branch to `main` so `git push heroku main`.
- Disabled inputs returns `None` when submitted to server using `POST` method.

Useful resources:
- 
- [ThirdWeb](https://thirdweb.com): Start your Web3 development with the right SDK
- [Figma](https://figma.com): Sketch your ideas and process.
- [Locofy.ai](https://www.locofy.ai/): Turn your Figma design into production-ready front-end code (supports HTML, CSS, React, Tailwind CSS and more)
- [Notion](https://notion.so): A goal without a plan is just a dream.
- [Animate.css](https://animate.style/): Adding animation to elements with just a class name.
- [Animate on Scroll Library](https://michalsnik.github.io/aos/): Animation but with a condition: on scroll of the user.
- [w3school.com](https://www.w3schools.com/): Extremely helpful. Learn all syntax you will ever needed for web development ranging from HTML, CSS to AJAX, SQL, etc.
- [Stack Overflow](https://stackoverflow.com/): Can't stress enough.
- [StackEdit](https://stackedit.io): User-friendly Markdown editor.
- [Imgbb](https://imgbb.com): Free image hosting.
- [Chris Luno](https://www.youtube.com/channel/UCjNpCOBtNDyk7kcs-wrX_dg): Dope music to code to.

### Thank you for reading until the end of my project. This was CS50.
