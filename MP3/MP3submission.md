<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Zahooruddin Zohaib Mohammed (zm254)</td></tr>
<tr><td> <em>Generated: </em> 11/27/2023 1:14:09 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/zm254" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T22.28.26image.png.webp?alt=media&token=c14a89da-2adc-471e-a421-fe1f3ff8b2a8"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of landing page with ucid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T22.29.47image.png.webp?alt=media&token=be70b5e9-7211-48ec-a393-872c1e643d52"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T22.30.36image.png.webp?alt=media&token=3527c364-e70e-4a4a-bd39-2d68c156e95d"/></td></tr>
<tr><td> <em>Caption:</em> <p>navbar changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T22.42.40image.png.webp?alt=media&token=8a952cf1-2ca3-409a-8567-172bc704502e"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing links changed wrt to respective page<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T22.43.48image.png.webp?alt=media&token=3850da8a-6c99-4b0d-aac4-bd89b3ce5c1a"/></td></tr>
<tr><td> <em>Caption:</em> <p>webpage loockup import Data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T22.44.46image.png.webp?alt=media&token=831a9d8a-810f-4d8e-a566-137b8a5fa4ec"/></td></tr>
<tr><td> <em>Caption:</em> <p>data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.43.24image.png.webp?alt=media&token=52b82d09-7d6d-4b9f-a382-bdc4e592a259"/></td></tr>
<tr><td> <em>Caption:</em> <p>checking that the file is a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.44.10image.png.webp?alt=media&token=b0a7325e-d578-4cbc-b8f6-ecd6226717a5"/></td></tr>
<tr><td> <em>Caption:</em> <p>read the csv file as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.48.09image.png.webp?alt=media&token=bf3bd701-5551-44fb-83b9-77105fe8e0b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>extracting the organization data and append it to the organization list as a<br>dict for each row that contains all of the required fields. Hint: see<br>the sql query related to it<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.50.04image.png.webp?alt=media&token=d2b5941c-b3b7-450c-a6ad-14b547d7b67f"/></td></tr>
<tr><td> <em>Caption:</em> <p>extracting the donation data and append it to the donation list as a<br>dict for each row that contains all of the required fields. Hint: see<br>the sql query related to it (also note how the name is retrieved)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.51.46image.png.webp?alt=media&token=18c53eea-ff48-4699-8ffb-3ab560db69e1"/></td></tr>
<tr><td> <em>Caption:</em> <p>display a flash message about the number of organizations that were successfully processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.52.32image.png.webp?alt=media&token=37fa2fca-1e13-4f8c-91a3-ae255d3b5d9e"/></td></tr>
<tr><td> <em>Caption:</em> <p>display a flash message (info) if no organizations were eligible/processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.53.22image.png.webp?alt=media&token=19070788-d188-4aff-aef3-8de63b492239"/></td></tr>
<tr><td> <em>Caption:</em> <p>display a flash message about the number of donations that were successfully processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.54.07image.png.webp?alt=media&token=f4d0bfcb-5728-4635-97ed-0c9a78ed1d2b"/></td></tr>
<tr><td> <em>Caption:</em> <p>display a flash message (info) if no donations were eligible/processed<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-26T23.56.55image.png.webp?alt=media&token=95e9a530-b300-43f0-b7f8-25f50486794a"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot having correct url and create view.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.03.28image.png.webp?alt=media&token=3444ebed-9b24-41c1-8784-e8506cc57924"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the code part-1.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.04.18image.png.webp?alt=media&token=b982ae1e-6e6d-4c46-ac0b-2d028987a5e6"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the following code part-2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.32.55image.png.webp?alt=media&token=e6b27dd4-c13d-4638-bcfe-c22a31da7b58"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit view<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.34.09image.png.webp?alt=media&token=567ffb27-30d8-4f2a-9497-191cc96084e2"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the page having proper ucid and no proper list of donation (no<br>filter)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.35.28image.png.webp?alt=media&token=e8a6c087-e101-4567-9781-737017f17693"/></td></tr>
<tr><td> <em>Caption:</em> <p>filter applied with organization_name and Donor_firstname<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.37.26image.png.webp?alt=media&token=20fc07f8-882a-457c-ba48-e0160ee66f09"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot with the code of search page part-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.38.23image.png.webp?alt=media&token=eed1aa73-d503-4e07-b387-5008256b97f9"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot with the code of search page part-2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.38.58image.png.webp?alt=media&token=e92eb6f7-898e-4a5a-92a7-f710d313793f"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot with the code of search page part-3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.39.29image.png.webp?alt=media&token=379395a0-f4a0-4f6c-928e-698372658d72"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot with the code of search page part-4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.42.02image.png.webp?alt=media&token=3150327d-2f1c-4e4b-baf3-53c43efc4dbd"/></td></tr>
<tr><td> <em>Caption:</em> <p>search-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.42.42image.png.webp?alt=media&token=1224769f-54c1-47b2-a2ac-5cd87371ee94"/></td></tr>
<tr><td> <em>Caption:</em> <p>search-2 to6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.43.15image.png.webp?alt=media&token=98579f20-7813-467c-9f0c-40b0595b16a3"/></td></tr>
<tr><td> <em>Caption:</em> <p>search 7&amp;8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.44.34image.png.webp?alt=media&token=de718163-7ddc-4dbe-ae30-ca7df49f1d01"/></td></tr>
<tr><td> <em>Caption:</em> <p>search 9&amp;10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.45.40image.png.webp?alt=media&token=2f8f0dab-ce50-4331-bf78-1b038176d35b"/></td></tr>
<tr><td> <em>Caption:</em> <p>search 11&amp;12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.53.11image.png.webp?alt=media&token=00ff6e09-a472-4f23-a2c5-492744176342"/></td></tr>
<tr><td> <em>Caption:</em> <p>add 1-3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T00.54.01image.png.webp?alt=media&token=b1a208fe-0e26-4350-95c0-d1dea803e4b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>add 5-9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.03.05image.png.webp?alt=media&token=8ff46456-9509-41e7-9553-260ca96945c6"/></td></tr>
<tr><td> <em>Caption:</em> <p>add 10-11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.07.30image.png.webp?alt=media&token=73d2080e-fb57-45db-8694-0744fafec054"/></td></tr>
<tr><td> <em>Caption:</em> <p>add 12-14<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.08.48image.png.webp?alt=media&token=a993a3cf-3fb8-40f4-b676-3870d344af57"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.09.37image.png.webp?alt=media&token=bb7a484d-7cd9-43ba-b488-b558b0a7f5a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>add 2-7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.13.56image.png.webp?alt=media&token=e8710180-1a8b-474d-8161-2b1a85414c70"/></td></tr>
<tr><td> <em>Caption:</em> <p>add 8-11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.15.34image.png.webp?alt=media&token=1a3587dc-6db1-4f3c-b59e-d2736780709e"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit 12<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.16.20image.png.webp?alt=media&token=7c7d9dcc-001b-4211-8b05-3ed21cdc7efc"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit 13-15<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T01.16.54image.png.webp?alt=media&token=d6ff4f30-b5a4-477e-8c2a-3c5bb664fb77"/></td></tr>
<tr><td> <em>Caption:</em> <p>del 1-5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T03.36.05image.png.webp?alt=media&token=48662566-9e86-4ca0-a376-81ab871bf7ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot previewing successfull del<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T03.39.09image.png.webp?alt=media&token=f4f8aca7-a236-4a6c-bf5b-3c54e9ffdeed"/></td></tr>
<tr><td> <em>Caption:</em> <p>search view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T03.45.49image.png.webp?alt=media&token=a5121468-5c3b-42f6-bf1d-f9891654820e"/></td></tr>
<tr><td> <em>Caption:</em> <p>create view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T04.40.44image.png.webp?alt=media&token=f357e56b-7991-4b9e-94d3-fe5383e2a518"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.34.20image.png.webp?alt=media&token=7d424347-1d1c-4d08-ad17-a03b1cba0d98"/></td></tr>
<tr><td> <em>Caption:</em> <p>manage_organization part-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.34.58image.png.webp?alt=media&token=4a327d6b-c46c-43b0-97e8-f7d8d9317f87"/></td></tr>
<tr><td> <em>Caption:</em> <p>manage_organization part-2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.30.15image.png.webp?alt=media&token=b7c660e1-9784-4595-8385-a25a981a505e"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route without filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.30.58image.png.webp?alt=media&token=ff24089d-c541-41d6-929a-222469e9cbc9"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route with filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.35.39image.png.webp?alt=media&token=bf0c424b-5ea6-4a12-a348-a58bfda5ba81"/></td></tr>
<tr><td> <em>Caption:</em> <p>list_organization part1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.36.07image.png.webp?alt=media&token=2a0bfbb2-342d-4685-a224-5c35f55c6494"/></td></tr>
<tr><td> <em>Caption:</em> <p>list_organization part-2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.36.35image.png.webp?alt=media&token=9bd82d99-c6df-4c5f-8b67-772ee326a603"/></td></tr>
<tr><td> <em>Caption:</em> <p>list_organization part-3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.39.16image.png.webp?alt=media&token=5b7861a5-f35c-46c6-bdf5-8e3e67560b66"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route part-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.39.34image.png.webp?alt=media&token=154dcca6-7a57-4538-93ef-59bd91d9b2da"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route part-2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.40.03image.png.webp?alt=media&token=a84b889b-77d4-48d2-b364-abce59a4a90e"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route part-3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.40.57image.png.webp?alt=media&token=f96260c2-cb0a-4498-a75e-d1d8aa438777"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route part-4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.41.59image.png.webp?alt=media&token=b908e495-e2bd-4cec-b3b3-2db6a8f92eb3"/></td></tr>
<tr><td> <em>Caption:</em> <p>add route part1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.42.30image.png.webp?alt=media&token=0819f2ef-cb59-4b29-8f79-8b329c856a11"/></td></tr>
<tr><td> <em>Caption:</em> <p>add route part2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.43.21image.png.webp?alt=media&token=d48447c2-d45a-4e82-9247-a24d80594ed3"/></td></tr>
<tr><td> <em>Caption:</em> <p>add route part3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.44.31image.png.webp?alt=media&token=7ef45227-4c84-449b-9bcb-9fba3f237009"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit route part1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.44.53image.png.webp?alt=media&token=52d78e71-6ad7-42eb-8515-712c2f8b28e9"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit route part2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.45.28image.png.webp?alt=media&token=716bcf43-57ed-4a87-bfeb-7f9af0817af8"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit route part3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.47.03image.png.webp?alt=media&token=10dfffe1-7bbd-4f07-abd5-6bacffe4c26b"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit route part4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.47.29image.png.webp?alt=media&token=b163c476-cded-4e6d-bdd5-5ec6a3f36dd1"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit route part5<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.48.17image.png.webp?alt=media&token=32d8f32a-7334-42f1-bc3d-4e34e9e339d9"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.49.25image.png.webp?alt=media&token=1f9de877-d157-47bd-8a7e-88e156babe12"/></td></tr>
<tr><td> <em>Caption:</em> <p>successfully deleted website prespective<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.50.52image.png.webp?alt=media&token=29b71dd3-64a4-4586-9d46-3755c762ba82"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.00.03image.png.webp?alt=media&token=93930972-99b3-4979-9786-2a286319ace8"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.00.13image.png.webp?alt=media&token=2fc8f1b6-6ccc-4719-a98e-5f23f4973b91"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.00.32image.png.webp?alt=media&token=acaed6d5-a8e2-4cbd-bcdb-b059e8185605"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.02.29image.png.webp?alt=media&token=968ecf14-3af6-4dfa-8e84-1b91c757a94f"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.02.39image.png.webp?alt=media&token=39dbd7a7-1ef3-4acb-902f-51eab1cd2751"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.02.50image.png.webp?alt=media&token=98dd033c-2f03-464a-9083-7245761372f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.03.25image.png.webp?alt=media&token=d1bf1430-68bb-472a-9d9d-71bfdf597f20"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.03.37image.png.webp?alt=media&token=f885b0fb-dc61-4a58-9a26-59d392979540"/></td></tr>
<tr><td> <em>Caption:</em> <p>All of the test case passed of test_donations.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.51.40image.png.webp?alt=media&token=239a5642-f5be-45e8-b59b-8b3c7d5047a0"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.03.52image.png.webp?alt=media&token=e01f428f-4e80-45d8-abf6-8f381eecd4ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.04.02image.png.webp?alt=media&token=7d135e1f-2f66-4d83-abc5-2177988d587f"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.04.13image.png.webp?alt=media&token=5d751feb-eca4-4397-b0f8-9b6a9ea331eb"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.04.23image.png.webp?alt=media&token=d1901aa0-5def-4d5b-98ea-a3c2f5366256"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.04.33image.png.webp?alt=media&token=d9db20aa-3be0-4447-9c9a-f94ef4dd4096"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.04.45image.png.webp?alt=media&token=e218698b-ea52-4164-937f-11fbf2aa2a0e"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.04.54image.png.webp?alt=media&token=08e81ed3-e60e-4640-b6d3-8acf6f7c7477"/></td></tr>
<tr><td> <em>Caption:</em> <p>all test passed of test_organization.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.52.18image.png.webp?alt=media&token=0ab983eb-3fa7-4392-ba01-54d1c0457f6b"/></td></tr>
<tr><td> <em>Caption:</em> <p>test passed <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.05.13image.png.webp?alt=media&token=1cf58c43-8ce0-418f-a539-9ea4b0f45a35"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of passing test_upload.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.52.47image.png.webp?alt=media&token=62088b51-b805-43da-ba10-b1578c4026ce"/></td></tr>
<tr><td> <em>Caption:</em> <p>test passsed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T06.05.38image.png.webp?alt=media&token=2536c0c8-7dc6-4231-bc68-23364432e511"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of passing test_index.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>all of the test passed&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/zahooruddinmohammed/zm254-is601-007/pull/44">https://github.com/zahooruddinmohammed/zm254-is601-007/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.53.54image.png.webp?alt=media&token=3479dd07-1c8b-4d61-8ec9-36319a31b6c6"/></td></tr>
<tr><td> <em>Caption:</em> <p>committing history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.55.31image.png.webp?alt=media&token=71bbf3d2-52aa-4e79-991f-ac266458e62a"/></td></tr>
<tr><td> <em>Caption:</em> <p>waka time<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.56.47image.png.webp?alt=media&token=3e2e9a2d-8b93-4731-8650-95c8ab2247e2"/></td></tr>
<tr><td> <em>Caption:</em> <p>waka time<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-11-27T05.57.42image.png.webp?alt=media&token=f97ea1ef-7021-4f64-83e3-a978acb75eb2"/></td></tr>
<tr><td> <em>Caption:</em> <p>waka time<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-zm254-td-6c9f9bcc3f2f.herokuapp.com/">https://is601-007-zm254-td-6c9f9bcc3f2f.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/zm254" target="_blank">Grading</a></td></tr></table>