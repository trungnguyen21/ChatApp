# Freely - A Chatapp built on Web3
### Video Demo: TODO
### Description:

Welcome to Freely - a Web3 application that enables decentralization in a simple chat app! The webapp was written in Python (Flask), Javascript, HTML and CSS.

Features:
- Fully decentralized: With the use of SocketIO, you can still chat asynchronously without sacrificing privacy. The chat app was serverless so no one can read your messages!
- Metamask authentication: Simply connect your wallet that holds our [Edition-drop NFT](https://portal.thirdweb.com/pre-built-contracts/edition) and enter your username of choice, you are in!
- NFT integration: I strongly believe that NFTs are more than apes and PNGs, they are the future of identity and validation! 
- Modern design: I leverage the use of [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/): 
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

Simple widget embeded on the page from ThirdWeb. The page then handles Wallet connection and gasless minting.

**NFT**: Non-fungible Token

**Edition-drop NFT**: One NFT, multiple owners. [The Pioneer NFT](https://thirdweb.com/mumbai/edition-drop/0xdc024d592D197053BdEcB966121C323A846EF1a5?tabIndex=0) acts as a pass to access content on the webpage. 

**Mumbai Testnet**: [A Testnet on Polygon Network](https://docs.polygon.technology/docs/develop/network-details/network/). Fast transactions with little to no gas fee, uses MATIC token. 

**Gasless minting**: I followed ThirdWeb documentation and set up a Relayer with an automated task to pay the gas fee for the minting process on [OpenZepplin Defender](https://www.openzeppelin.com/defender). Users can now mint the NFT without the need to pay any fees.
