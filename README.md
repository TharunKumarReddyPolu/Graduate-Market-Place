## Hello! Good to see you here...👋
# Welcome to the `Graduate Market Place`
 ✏️ An online marketplace designed and developed for students which serves as a common platform to sell and buy used/new products.<br>
 ✏️ One Stop solution for e-Exchange of products within a student(Graduates, Undergraduates and Postgraduates) community.<br>
 ✏️ Here you can post the product you want to sell or look for products you wanted to buy from other fellow students.<br>

 📌 Tech Stack used: Python, HTML, TailwindCSS, Django, SQL Database<br>

### If you're an open-source developer/enthusiast, Feel free to Contribute 😁🛠 Be it code or non-code 😉
## Steps to follow📃

### 1. Fork the project 🔪 (_This creates a copy of the project into repositories of your GitHub account_)

   [Fork Button](https://github.com/TharunKumarReddyPolu/Graduate-Market-Place)

### 2. Clone the forked repository 📥

  You need to clone (download) it to your local machine using below command in terminal
```bash
   $ git clone https://github.com/TharunKumarReddyPolu/Graduate-Market-Place.git
```
> This creates a local copy of the repository in your local machine 📂

  Once you have cloned the `Graduate-Market-Place` repository into your local machine, move➡️ into that folder using the change directory `cd` command on Linux/ Mac/ Windows
```bash
   $ cd Graduate-Market-Place
```
### 3. Let's Set it up 🔧⚙️
Run the following commands to verify that your _local copy_ has a reference to your _forked remote repository_ on Github
```bash
   $ git remote -v
```
It should display the below output
```
  origin  https://github.com/Your_Username/Graduate-Market-Place.git (fetch)
  origin  https://github.com/Your_Username/Graduate-Market-Place.git (push)
```

Now, let us add the reference to the original `Graduate-Market-Place` repository using the below command 🔙
```bash
  $ git remote add upstream https://github.com/TharunKumarReddyPolu/Graduate-Market-Place.git
```
> The above command creates a new remote as `upstream`

To Verify the changes run the below command
```bash
  $ git remote -v
```
Output in console ☑️:
```
  origin    https://github.com/Your_Username/Graduate-Market-Place.git (fetch)
  origin    https://github.com/Your_Username/Graduate-Market-Place.git (push)
  upstream  https://github.com/TharunKumarReddyPolu/Graduate-Market-Place.git (fetch)
  upstream  https://github.com/TharunKumarReddyPolu/Graduate-Market-Place.git (push)
```
### 4. Keep in sync always♻️ (best practice🤝🏻) 
It is a better practice to keep the `local copy` in sync with the `original repository` and to stay updated with the latest changes. Run the below commands before making changes or in regular intervals to stay updated with the `base` branch

```
  # Fetch all remote repositories and delete any deleted remote branches
  $ git fetch --all --prune

  # Switch to the master branch
  $ git checkout master

  # Reset the local master branch to match the upstream repository's master branch
  $ git reset --hard upstream/master

  # Push changes to your forked Tweety-Virtual-Voice-Assistant repo
  $ git push origin master
```

### 5. Woohoo! You are ready for the first contribution 🌝
Once you are done with the above steps, you are ready to contribute to the `Graduate-Market-Place` project code.Add `new features` or Check out the `issues` tab of the `original repository` and solve them. Once you are done with your changes, submit your precious efforts with a `pull request`.

### 6. Working with the project 📦📥

To get started with the project set up, run the follow commands:
```bash
  # navigate to the virtual environment "gmp_env"
  cd gmp_env
  
  # activate the python virtual environment. Careful, S in Scripts is upper case 
  .\Scripts\activate
  
  # navigate to the project directory "gmp"
  cd gmp
  
  # To install the required packages for the project. run the below command
  pip install -r requirements.txt
```
> If any package installation is not specified above, then those packages are built-in with python.

```
  # Here's the main part, running the server
  python manage.py runserver
```
If you encounter below error after running the above command:
```
  python : The term 'python' is not recognized 
as the name of a cmdlet, function, script       
file, or operable program. Check the spelling   
of the name, or if a path was included, verify  
that the path is correct and try again.
At line:1 char:1
+ python manage.py runserver
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound:   
   (python:String) [], CommandNotFoundExcept   
  ion
    + FullyQualifiedErrorId : CommandNotFoundE  
   xception
```
Then change `python` to `python3` and re-run the command. This should solve the issue for you.<br>

> If the latest version of the packages is not working on your machine, then you can downgrade the version using the below commands
```bash
   $ pip uninstall package_name
   $ pip install package_name==specific version
```
For instance, If `Pillow` package latest version isn't working in your local machine, then do
```bash
   $ pip uninstall Pillow
   $ pip install Pillow==9.3.0
```
where `Pillow` refers to `package_name` and `9.3.0` refers to `previous version`/`specific version`

Hurray! you have the website up and running on your localhost and ready for your development.

### 7. Create a new branch 🌱
Whenever you are going to submit a contribution. Please create a separate branch using the below command and keep your `master` branch clean (i.e. synced with the remote branch)
#### Method 1:
```bash
  $ git branch Changetype_name
```
change type includes `bug fix`, `new feature`, `comments`, `enhancements` etc.

the name includes your `first name` or `last name`

After creating the branch above, run the below command to checkout/switch to the new branch created
```bash
  $ git checkout changetype_name
```
#### Method 2:
You can also create the branch and checkout to the desired branch using the single command below
```bash
  $ git checkout -b changetype_name
```

To add your changes to the branch. Run the below command ➕️
```bash
  $ git add . 
```
> Above command uses `period (.)` indicating all the files are added (or)
> to stage specific file changes, use the below command instead

```bash
  $ git add <file_name>
```

Then, Type in a message that is relevant for the code reviewer using the below command ✉️
```bash
  $ git commit -m 'relevant message'
```

Finally, Push your awesome hard work to your remote repository with the below command 📤🤝🏻
```bash
  $ git push -u origin changetype_name
```
Here, `changetype_name` refers to the branch in your remote repository

In the last, Navigate to your forked `Graduate-Market-Place` repository in the browser, where you will see `compare and pull requests`. Kindly click and then add a relevant `title` and `description` to your pull request that defines your valuable effort. 🥳✅️

### Latest Updates
> Yet to be published

## Help us improve the project better 📈🤗

Please discuss your concerns with [Polu Tharun Kumar Reddy](https://www.linkedin.com/in/polu-tharun-kumar-reddy/) before creating a new issue. 😉

_Please `STAR`⭐️ the repository if you like the content and code_**😁

_Also enable the `WATCH`👁 button to keep watching the updates on the repository_**😉

💯💻🧑‍💻👩‍💻 Happy Contributing 👩‍💻🧑‍💻💻💯
