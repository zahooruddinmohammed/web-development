<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Pumpkins</td></tr>
<tr><td> <em>Student: </em> Zahooruddin Zohaib Mohammed (zm254)</td></tr>
<tr><td> <em>Generated: </em> 10/23/2023 10:26:58 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/zm254" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4">https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4</a></li><li>Put them into a subfolder in your repository folder (I called my folder MP2)</li><li>Create a test folder as a subdirectory of MP2</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the below input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.21.46image.png.webp?alt=media&token=6222de7e-4b86-4c6c-a9c6-2016b4290d25"/></td></tr>
<tr><td> <em>Caption:</em> <p>calculate_cost function()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.23.12image.png.webp?alt=media&token=842b5b35-5039-4501-a5e3-027dc8709609"/></td></tr>
<tr><td> <em>Caption:</em> <p>calculate _cost function() call<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>Summary:<div>Keeping cost initially as zero</div><div>Adding the input item cost from the user in<br>a loop for every input of items(adding this to the initially maintained cost)</div><div>in<br>the end returning the final cost and round it</div><div>to 2 decimal numbers so<br>that it can be used as currency.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.45.49image.png.webp?alt=media&token=20b44ed4-fd5d-4a2c-8005-feede0b53230"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for out of stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.29.19image.png.webp?alt=media&token=86afefd5-1ba2-4967-8690-f21643e370c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>OutOfStockException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.30.39image.png.webp?alt=media&token=1c5ef4be-f46a-4e21-a254-692fc1ecbe26"/></td></tr>
<tr><td> <em>Caption:</em> <p>NeedsCleaningException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.32.01image.png.webp?alt=media&token=536357d6-ef0f-4fa3-9a7c-efdb05283244"/></td></tr>
<tr><td> <em>Caption:</em> <p>clean machine function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.33.34image.png.webp?alt=media&token=01ef9a83-7789-4d99-96db-d87b4cab76ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for NeedsCleaningException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.34.34image.png.webp?alt=media&token=68b5ece4-b480-4bdc-a24f-67326f507f5a"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.49.02image.png.webp?alt=media&token=01187eb3-5bf0-4f22-bd4c-622d5795168e"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for invalid choice<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.50.30image.png.webp?alt=media&token=9f59afae-6ce7-4b05-b79d-ebcb65c80d5f"/></td></tr>
<tr><td> <em>Caption:</em> <p>COndition for exceedingRemaningChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.39.16image.png.webp?alt=media&token=5404c4e3-2597-406b-8b40-998edd2f932e"/></td></tr>
<tr><td> <em>Caption:</em> <p>ExceededRemainingChoicesException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.51.35image.png.webp?alt=media&token=dca6f9e6-9b89-4aae-bb10-07c5eabced1d"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for invalid payment<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T16.41.32image.png.webp?alt=media&token=99e43ffc-f9ef-48e5-b9b0-debd8b62e93a"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidPaymentException Handling<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>OutOfStockException: In <span style="font-size: 14px;">our use function we are checking for</span><div><span style="font-size: 14px;">a<br>condition if our quantity is less than zero, if this condition is</span></div><div><span style="font-size:<br>14px;">true then we will raise the OutOfStockException exception and we</span></div><div><span style="font-size: 14px;">are calling<br>OutOfStockException in our main function and printing &quot;The</span></div><div><span style="font-size: 14px;">selected option is out<br>of stock. Please select another option&quot;</span></div><div><br></div><div><div><span style="font-size: 14px;">NeedsCleaningException: In our pick_face_Stencil function we<br>are checking for a condition if our&nbsp;</span>remaining_uses is less than equal to zero,<br>if this condition is true then</div><div><span style="font-size: 14px;">we will raise the NeedsCleaningException exception<br>and we are calling NeedsCleaningExceptionin our main function and printing &quot;Sorry, The machine<br>needs cleaning!</span></div><div><span style="font-size: 14px;">Please type &#39;yes&#39; to clean the machine&quot; and we will<br>ask the user</span></div><div><span style="font-size: 14px;">to type yes if the user enters clean then<br>we will reset the remaining_uses</span></div><div><span style="font-size: 14px;">to default and continue with our regular<br>pumpkin making.</span></div></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;"><br></span></div><div><div style=""><span style="font-size: 14px;">InvalidChoiceException: In&nbsp;</span>our pick_pumpkin, pick_face_stencil, pick_extras<br>functions we can checking for a condition where the existing pumpkin name,</div><div style="">&lt;span<br>style=&quot;font-size: 14px;&quot;&gt;face_stencil name and extras name should match the input from the user,<br>if</span></div><div style=""><span style="font-size: 14px;">the condition fails then we will raise the InvalidChoiceException excepition</span></div>&lt;div<br>style=&quot;&quot;&gt;<span style="font-size: 14px;">and will call the InvalidChoiceException in our main function and</span></div><div style="">&lt;span<br>style=&quot;font-size: 14px;&quot;&gt;print &quot;You&#39;ve entered an invalid choice. Please choose from the given options&quot;<br>and</span></div><div style=""><span style="font-size: 14px;">rerun the same stage again.</span></div></div><div style=""><span style="font-size: 14px;"><br></span></div><div style=""><div style="font-size:<br>14px;">ExceededRemainingChoicesException:&nbsp; In the initial state</div><div style="font-size: 14px;">we have set the remaining_stencil and remaining_extras<br>as 3. So whenever the user selects a face_Stencil and extras for the<br>same burger then remaining_face_Stencil&nbsp; and remaining_extras&nbsp; will decrease by 1. When remaining_face_Stencil&nbsp;</div><div style="font-size:<br>14px;">and remaining_extras&nbsp; becomes less than or equal to 0 then</div><div style="font-size: 14px;">we are<br>raising the ExceededRemainingChoicesException exception and ExceededRemainingChoicesException is called in our main function twice.<br>once while the user is selecting the face_stencil and the second time while<br>user is selecting the extras and it prints &quot;Sorry! You&#39;ve exceeded the maximum<br>number of face_stencil that you can select, please choose a topping&quot; and &quot;<br>Sorry! You&#39;ve exceeded the maximum number of extras; proceeding to the payment portal&quot;<br>respectively and moves to the next stage.</div><div style="font-size: 14px;"><br></div><div style=""><div style=""><span style="font-size: 14px;">InvalidPaymentException:<br>In our function handle_pay we are checking the the total</span></div><div style=""><span style="font-size: 14px;">price<br>of the pumpkin is equal to the price entered by&nbsp; the user.</span></div><div style="">&lt;span<br>style=&quot;font-size: 14px;&quot;&gt;If this condition is false then we are raising the exception InvalidPaymentException</span></div>&lt;div<br>style=&quot;&quot;&gt;<span style="font-size: 14px;">and it is called in our main function and prints the</span></div>&lt;div<br>style=&quot;&quot;&gt;<span style="font-size: 14px;">message &quot;You&#39;ve entered a wrong amount. Please try again :&quot; and<br>asks the</span></div><div style=""><span style="font-size: 14px;">user to reenter the amount.&nbsp;</span></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T17.30.50image.png.webp?alt=media&token=b2afb8f4-a813-452d-a58e-20f91e510a55"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case checks if the exception is raised when the out of stock<br>face stencil is choosen by user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T17.31.52image.png.webp?alt=media&token=fbaa8c39-0d84-493e-9f93-fa899cca4a67"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case checks if the exception is raised when the user chooses more<br>than 3 extras<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T17.32.26image.png.webp?alt=media&token=f606d508-6582-468d-bd92-252ab5ef06af"/></td></tr>
<tr><td> <em>Caption:</em> <p>this test case checks if the exception is raised when the user <br>chooses more than 3 face stencil<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T17.33.05image.png.webp?alt=media&token=a4ac78e8-c9e0-4344-b821-fb19eb4aea2b"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case chceks if the exception is raised when the user chooses more<br>than 3 extras<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T17.34.12image.png.webp?alt=media&token=11b55e00-2223-4c4c-833e-b8be927a2e04"/></td></tr>
<tr><td> <em>Caption:</em> <p>chekcs if the total cost returned by the calculate_cost is correct<br>checking for all<br>possibilites like pumpkin,face_stencil,extra  using random module<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T17.35.29image.png.webp?alt=media&token=75292e37-8372-46f9-a42a-ecf3876254eb"/></td></tr>
<tr><td> <em>Caption:</em> <p>function is used for total sales using fixture<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-20T17.36.15image.png.webp?alt=media&token=824b0743-398c-40e3-8ced-e0883e104cdb"/></td></tr>
<tr><td> <em>Caption:</em> <p>used for total_products to check if the total_products is increased properly<br>testing using fixtures<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-24T02.04.11image.png.webp?alt=media&token=1772d62c-64a9-4bc7-8923-5e0c3660738e"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing test_first_Selection case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-24T02.06.16image.png.webp?alt=media&token=c7caaebb-7a99-442d-a949-aa9d2680acc9"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing all the test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 14px;">Test 1 -</span></div><div><span style="font-size: 14px;">pumpkin must be the first selection -<br>The order&nbsp;</span>of the selection has to be correct and the exception is raised<br>if the order is not correct. For the order to be correct the&nbsp;bun<br>has to be correct. In the above screen short we are testing by<br>giving a invalid order.&nbsp;</div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">Test 2 -</span></div><div><span style="font-size:<br>14px;">can only add face_Stencil if they're in stock - This test case&nbsp;</span>checks if<br>the face_Stencil are in stock and also checks if the exception is raised<br>when the out of stock face_Stencil is chosen by the user.</div><div><br></div><div><span style="font-size: 14px;">Test<br>3 -</span></div><div><span style="font-size: 14px;">&nbsp;can only add extras if they're in&nbsp;</span>stock - This test<br>case checks if the extras are in stock and also checks if the<br>exception is raised when the out of stock extras is chosen by the<br>user.</div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">Test 4&nbsp;</span>-</div><div>&nbsp;Can add&nbsp;up to 3 face_Stencil of any combination<br>-This test case checks if the user has not added more than 3<br>face_Stencil and checks if the exception is raised&nbsp;when the user chooses more the<br>3 face_Stencil.</div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">Test 5 -</span></div><div><span style="font-size: 14px;">&nbsp;Can add up to<br>3 extras of any&nbsp;</span>combination - This test case checks if the user has<br>not added more than 3 extras and checks if the exception is raised<br>when the user chooses more the 3 extras.</div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">Test 6</span>-</div><div>&nbsp;cost<br>must be calculated properly based on the choices -&nbsp; This functions checks if<br>the total cost returned by the calculate_cost is correct. It is</div><div><span style="font-size: 14px;">checking<br>for all scenarios like pumpkin, face_Stencil and extra using random module.&nbsp;</span></div><div><span style="font-size: 14px;"><br></span></div><div>Test<br>7 -</div><div>&nbsp;Total Sales (sum of costs) must be calculated properly&nbsp; .This functions test<br>for total_sales. It checks if the total_sales is calculated properly, we are doing<br>this test case using fixtures.</div><div><span style="font-size: 14px;">&nbsp;</span></div><div><span style="font-size: 14px;">Test 8 -</span></div><div><span style="font-size: 14px;">&nbsp;Total<br>pumpkin should&nbsp;</span>properly increment for each purchase - This function is for total_products to<br>check if the total_prodcuts&nbsp; is increased properly we are testing this function using<br>fixtures.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/zahooruddinmohammed/zm254-is601-007/pull/13">https://github.com/zahooruddinmohammed/zm254-is601-007/pull/13</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>i had to learn in depth about test cases to grab strength over<br>this. this project took me a while to understand what was being asked<br>and setting up the virtual environment took me sometime adding to the workspace<br>and all. had quite a new things to understand about.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>Output 1<br></p>
</td></tr>
<tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>Output 2<br></p>
</td></tr>
<tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/zm254" target="_blank">Grading</a></td></tr></table>