### Some notes for reviewers

1. This is my first time using flask for building a web app and I was unsure about the typical project structure, so I used the mvc pattern from Java and split the project into 3 layers:
- controller - request handling
- service - business logic
- model/repository - data

2. There was no requirement to persist data, hence I did not integrate a database. All data persists in session only.

3. All requests return json response. In case of POST requests an empty response is returned. Additionally, I try to limit exposing internal functionality, hence all exceptions are handled, logged and a respective HTTP response code (400/404) is returned instead.

4. No additional libraries were used as the task did not specify if they are allowed or not. However, I would typically create swagger documentation for endpoints, perhaps using the `flasgger` library.

5. Calling `/transfer` endpoint should initiate a transaction, to ensure atomicity in case of an unexpected error on either side. To handle this properly I would need to integrate a database, which would be the first improvement to make.

6. `id` in `Account` and `User` were made hidden from the constructor as the idea is that the id is generated upon inserting a record into a db, making it final and unique.

7. All functionality is tested in the `tests` folder.