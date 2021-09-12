# symfoni

This application is for listening to your favorite songs and creating personalized
playlists.

## Database schema

[x] User table

  1. user_id: int, primary key, auto-increment
  2. username: varchar(50) not null, unique
  3. password: varchar(25) not null
  4. date_of_joining: timestamp not null
  5. last_login: timestamp

[x] Artist table

  1. artist_id: int, primary key, auto-increment
  2. name: varchar(50) not null

[x] Song table

  1. song_id: int, primary key, auto-increment
  2. name: varchar(50) not null
  3. artist_id: foreign key to Artists table
  4. url: varchar(200)

[x] SongLike table

  1. song_like_id: int, primary key, auto-increment
  2. song_id: foreign key to Songs table
  3. user_id: foreign key to Users table
  4. Unique constraint between song_id and user_id

[] Playlist table

  1. playlist_name: varchar(75) not null
  2. playlist_id: int, primary key, auto-increment
  3. songs: ManyToMany to song table
  4. created_by: foreign key to user table

## Common HTTP verbs

When you want to access data from the server, you normally use an HTTP method (verb) to
request that data. Some common methods are:

- **GET**: It is the most common method, you use it when you want to just GET data from the
  server.
- **POST**: It is used when you want to edit data on the server.
