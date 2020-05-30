# PICKYeats - Backend

This is the backend API for the PICKYeats mobile app. The API allows the frontend to manage users, parties, liked restaurants, and matched restaurants.

Frontend respository: https://github.com/kadrianne/pickyeats-backend

## Built With
Frontend: JavaScript, React Native v0.62.2, Redux, [React Native Elements](https://react-native-elements.github.io/)<br>
Backend: Python 3.8.2, Django v3.0.6, Django Rest Framework v3.11.0, PostgreSQL v12.2

API for business data: [Yelp Fusion](https://www.yelp.com/fusion)

The app is currently only build for and tested with an Android device (Pixel 3 XL) using an Android Studio emulator.

## App Features

### 

## Challenges

This is my first project coding in Python and working with Django. Using Django REST Framework simplified much of the code, but I felt it was a steep learning curve in understanding how Django works by itself and what Django REST Framework was doing behind the scenes.

Extending the user model and implementing authentication was also a challenge as there are a few ways to handle it and it's much easier to do earlier on. Understanding how the built-in auth works took a bit of time as it uses token authentication, but not necessarily JWT, which is what I'm more familiar with.

## Future Implementation

- Add permissions (full authorization)
- Refactor APIs and data relationships

## Collaboration

1. Fork and/or clone this repo & the backend repo - https://github.com/kadrianne/pickyeats-backend
2. Create PostgreSQL database `createdb pickyeats`
3. Migrate database tables in backend: `python3 manage.py migrate`
4. Run backend server: `python3 manage.py runserver`
5. Install dependencies on frontend: `npm install`
6. Run frontend server: `npx react-native run-android`
7. Checkout new branch
   
I have a GitHub project board with a few backlog items here: https://github.com/kadrianne/pickyeats/projects/1<br>
If you'd like to collaborate on this project, please email me: kristine.a.du@gmail.com
