<h1>Random Password Generator in Python</h1>

<h2>Description</h2>
My 2nd Python project that generates random passwords for users 
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>PyCharm CE</b>
- <b>MacOS 12.5</b> 

<h2>Program walk-through:</h2>

<p align="center">
Import the Random and String function (this is to retrieve the upper and lower case alphabets, punctuation and special symbols. <br/>
<img src="https://imgur.com/W5Snv0e.png" height="80%" width="80%" 
<br />
<br />
Ask the user to input password preferences / requirements. Make sure values are integers to work:  <br/>
<img src="https://imgur.com/n8JnQwg.png" height="80%" width="80%" 
<br />
<br />
Create an empty list to contain pw characters. Create a for loop to generate random numbers / letters / symbols based on the user's input. Use range function to generate a sequence of numbers from 1 to the pw characters length requested by the user. Add the +1 to make the range inclusive of the upper limit of the range of pw characters. Then add the random.shuffle function to the pw list to randomly shuffle the characters. Finally, use the join function to concatenate all the generated elements into a single neat password string. Use the empty string '' as a separator between each element. <br/>
<img src="https://imgur.com/OBTTb6L.png" height="80%" width="80%" 
<br />
<br />

