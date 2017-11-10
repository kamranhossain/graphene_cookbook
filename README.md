# Graphene Cookbook

Example Application with django graphene package(Docs) with reformatting structure.
This repo is the walkthrough in the docs of graphene_django. There are some typos on docs and some deprecated codes. All these things fixed in this repo. So please follow the docs and this repo to make your code error free.

### Setup Steps

1. git clone https://github.com/kamranhossain/graphene_cookbook.git
2. cd graphene_cookbook
3. virtualenv venv
4. source venv/bin/activate
5. pip install -Ur requirments/base.txt
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py createsuperuser
9. python manage.py runserver
10. Goto the localserver 127.0.0.1:8000/graphql
11. Go to localhost:8000/graphql and type your first query!

```graphql
query {
  allIngredients {
    id
    name
  }
}
```
12. We can do that with the following query for getting relations:
```graphql
query {
  allCategories {
    id
    name
    ingredients {
      id
      name
    }
  }
}
```

13. Get single objects. Lets query category:

```graphql
query {
  category(id: 1) {
    name
  }
  anotherCategory: category(name: "Dairy") {
    ingredients {
      id
      name
    }
  }
}
```
