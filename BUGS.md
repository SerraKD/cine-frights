# **Bugs**

# **Table of contents**

1. [**Fixed Bugs**](#fixed-bugs)
2. [**Unfixed bugs**](#unfixed-bugs)

## **Fixed Bugs**

During the development, I documented the bugs I encountered in projects' [Kanban Board](https://github.com/users/SerraKD/projects/4/).

| Issue | Bug | Description | Fix | Commit |
| :--- | :--- | :--- | :--- | :--- |
| [#19] | Bug: Movie ratings| Description: Integer field for Imdb ratings does not accept decimals. Slug field for rotten tomatoes does not accept "%" sign. | Both changed to textField, added max length to 3 characters. | [46a9275](https://github.com/SerraKD/cine-frights/commit/46a92759974fa5a1fca2bcdfcbdecae10fb416b7) |
| [#20] | Bug: Comments user ratings | Description: Trying to add a comment with a user rating, raises TypeError. Exception Value: unsupported operand type(s) for  'str' and 'int' | Str dunder method was trying to return self.content(str) and self.user_rating(int) together. Adding forgotten semicolon to both resolved the error. | [42c77fb](https://github.com/SerraKD/cine-frights/commit/42c77fb8657478bdd558186807cfef0c1c8225a5) |
| [#21] | Bug: ImproperlyConfigured |  Description: File "/workspace/cine-frights/frights/models.py", line 3, in from django.contrib.auth.models import User, File "/workspace/cine-frights/frights/views.py", line 4, in from models import Movie, Comment django.core.exceptions ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings. | Created a new app called movies, moved all files from previous app frights , migrated all changes and deleted frights app fixed the issues. To make sure i took correct steps i added Pylint and installed a newer version of Django to the project. | Bug fix completed with the last commit: [74b3aa9](https://github.com/SerraKD/cine-frights/commit/74b3aa9ec7c59f9e5c15e509046fd14eb3c8b08b) |
| [#22] | Bug: Approved Movie posts | Description: Approved movie posts are not visible on the home page. | Loop in the index.html wasn't looping over the movies. Replaced home_page_view with object_list in index.html | [c142c13](https://github.com/SerraKD/cine-frights/commit/c142c1370a5ae4a8a4211aad82e3f2726daec24b) |
| [#23] | Bug: Heroku Build failed | Description: ModuleNotFoundError: No module named 'emoji_picker'! Error while running '$ python manage.py collectstatic --noinput'. | After downloading django emoji picker extention I forgot to add it to settings.py and requirements.txt  | [26461f2](https://github.com/SerraKD/cine-frights/commit/26461f25235c6cbd4f76e02e7c2858f57096e491) |
| [#24] | Bug: Carousel Buttons | Carousel elements are looping through movies correctly, but previous and next buttons are not showing up and working. | Turns out i installed to workplace newer version of bootstrap but using the old bootstrap docs. Updating bootstrap to 5.2 and using the code from 5.2 docs fixed the error. | [912049f](https://github.com/SerraKD/cine-frights/commit/912049fa76638f4e50e5c628964dc53a4cbe5314)  [e09d561](https://github.com/SerraKD/cine-frights/commit/e09d5617d183f3cf47d654aec696e40ae8595063) |
| [#25] | Bug: User Comments | Description: User comments for a certain movie was appearing under every movie post. | Fixing the variable names for accessing movie comments created in movie detail view fixed the error. | [26cc377](https://github.com/SerraKD/cine-frights/commit/26cc37744904de6337c21df0ca654727ca3efad2) |
| [#26] | Bug: Edit Comment | Description: Although delete comment function works, edit button does not work. | Tried console.log within comments.js, prints to console in port so clicking on button function works. & comments.js was looking for an element in movie_detail template called id_body, but in the template id was id_content. Fixing the calling in comments.js as id_body resolved the error. | [ac55fcc](https://github.com/SerraKD/cine-frights/commit/ac55fcc13c0f7d95f4ea419e6bd433db4501f384) |
| [#27] | Bug: Make migrations | Description: After deleting the user ratings in Comments model, this error showed up when trying to do migrations django.db.utils.ProgrammingError: column "user_rating" of relation "movies_comment" does not exist | running python3 manage.py migrate movies zero & doing migrations again with python3 manage.py migrate fixed the error. | - |
| [#29] | Bug: Newsletter Unsubscribe | Description: Although subscribe to newsletter function works, unsubscribe function doesn't remove the email from database. | 1.Added print statement and print("FORM ERRORS: ", member_form.errors), the function was trying to create a new instance. / 2.Added redirect to newsletter url. / 3.Deleted if valid statement and member form, added email. / 4.Changed request message to error, member objects name to member. / 5.Wrote try-catch statement for the member email that is not in the database. | [e429901](https://github.com/SerraKD/cine-frights/commit/e4299013593657b4d7f1f6fb4aca3eeda6b0801f) [f8640c8](https://github.com/SerraKD/cine-frights/commit/f8640c8f7df302c657a31c0c0c779280c9c51afb) [792f074](https://github.com/SerraKD/cine-frights/commit/792f074de64978a5448777fdf02cfc4b5b9ecbb0) [9cb6b45](https://github.com/SerraKD/cine-frights/commit/9cb6b45d80ffa9a6911992e024798248fdf8b1aa) [de36ad9](https://github.com/SerraKD/cine-frights/commit/de36ad903566f98ed0115150f74c4e16cd7cabce) |


> **Issue [#21](https://github.com/SerraKD/cine-frights/issues/21) Bug: ImproperlyConfigured**

All Commits Regarding to app change:

- add pylint as default formatter in settings.json [220b750](https://github.com/SerraKD/cine-frights/commit/220b7504b69cf2440947a6ba73ebbd79e9f4afa8)
- Install newer version of django, add it to requirements.txt [edc0fd9](https://github.com/SerraKD/cine-frights/commit/edc0fd95fa45082780931c4a8c2b35d95b871c87)
- Start a new app called movies [47bfefe](https://github.com/SerraKD/cine-frights/commit/47bfefeadcb08aba6e547117e7934d52707845d9)
- Change path for app in urls.py [ba5243a](https://github.com/SerraKD/cine-frights/commit/ba5243acce8d5730a6743431ffaa459c1367ae69)
- Add new app movies to settings.py [0497efc](https://github.com/SerraKD/cine-frights/commit/0497efcef82ea6cfcf138b75a9f4f8c4f1eaea67)
- move admin.py code from frights app to movies app [e7ceba6](https://github.com/SerraKD/cine-frights/commit/e7ceba6fe6f2191b19960f1b03541ddca3849cc6)
- move models.py code from frights app to movies app [5ac80b7](https://github.com/SerraKD/cine-frights/commit/5ac80b7cdf13938b0bc3589763f85edc5d234d26)
- move urls.py code from frights app to movies app [e532398](https://github.com/SerraKD/cine-frights/commit/e5323984180477c6b40986b93f9eff709129b374)
- move views.py code from frights app to movies app, change template path to movies [7c6f4fa](https://github.com/SerraKD/cine-frights/commit/7c6f4fa9a9c68d2377bba26d09e0b5597e4fb5ce)
- move index.html template code from frights app to movies app [99c5d90](https://github.com/SerraKD/cine-frights/commit/99c5d9011dbf62f71afb5d5a1f31b9d3f32e3df6)
- delete frights app and all its contents [d0963b0](https://github.com/SerraKD/cine-frights/commit/d0963b06654b83b5bfefec27aee5b7cb1b045497)
- recreate the file path as movies/templates/movies, move index.html into new file structure [99c5d90](https://github.com/SerraKD/cine-frights/commit/99c5d9011dbf62f71afb5d5a1f31b9d3f32e3df6)
- migrate the new app movies [714c912](https://github.com/SerraKD/cine-frights/commit/714c912aa64ce17ce7a279500ef21082652a2777)
- remove frights app from installed apps in settings.py [67cd2a](https://github.com/SerraKD/cine-frights/commit/a67cd2a8ac59c41d45cd8cee3ed6bbe7ea0d630e)
- remove frights path from imports in admin.py [74b3aa9](https://github.com/SerraKD/cine-frights/commit/74b3aa9ec7c59f9e5c15e509046fd14eb3c8b08b)

## **Unfixed bugs**

**[Go back to README.md](https://github.com/SerraKD/cine-frights#cine-frights)**