# Reactifying Django with portfolio blog engine

### Reactifying Django

1. Make changes in react app.
2. run `npm run collect`
3. build the react app
4. renames the build
5. copies the build to django's static files
6. collect static files so django can use it.

---

#### django-admin login details

- **email:** info@arsalaan.net
- **password:** something_simple

- **email:** haroldf01@gmail.com
- **password:** pass@123

#### Info about the database used and credentials

In this project the database is postgreSql.

- **databaseName:** portfolioblogdb
- **databaseUser:** postgres
- **password:** bobTheBuilder

---
### Listing Down Project Progress

1. Django User app added. This is the Custom user model with some forms as well. <u>Haven't been able to know the true purpose of those forms</u> but soon I will **find out and update it here.**

2. Was successfully able to setup semantic react UI and make 2 layouts work properly.

---
Have to start with these links

OAuth first part is getting executed perfectly token are gettings generated.

https://github.com/settings/applications/1207997
https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/

### Implement Categories

https://djangopy.org/how-to/how-to-implement-categories-in-django/

---

## Project Level URL Routing

We’ll be building the features in this order:

- URLs → views → serializers → models