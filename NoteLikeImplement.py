# From ChatGPT

# Question:
# The project KulBalam has a backendand a frontend, respectively written in Python and React. It is a marketplace, where users can trade items (put them up for sale and buy them), and a social network combined (where users can keep track of friends activities and communicate with each other).
# I want to implement a 'like' system for posts that:
# a) Create a database model (table) for 'postlikes', this model should (at least) have:
# - a reference to a post, indicating which post was liked
# - a reference to the user, indicating who liked the post
# - a datetime field, indicating when a like was created
# b) A user should be able to 'like' another users posts (not his own)
# c) A user should be able to 'unlike' any post he has an active 'like' on.
# d) The schemas model PostDisplay should be changed to be able to show how many 'likes' the post has and the code that produces posts to the front-end (e.g. swagger) should be adjusted to calculate this amount of likes per post.
# e) The schemas model PostDisplay should also be adjusted to be able to show if the currently logged in user has liked the post or not
# f) Add the number of likes for each post to the front-end project
# g) Add a way for a user to like (and unlike) a post

# Give me some ideas.

# Implementing a 'like' system involves both backend and frontend changes. Here’s a detailed plan to achieve this for your project, KulBalam:

# ### Backend (Python with FastAPI)

# #### a) Create a Database Model for 'postlikes'

# 1. Database Model:
#    - Define a new PostLike model in your ORM (SQLAlchemy).
#    - Ensure it has references to Post and User, and a created_at field for the timestamp.

# from sqlalchemy import Column, ForeignKey, Integer, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from .database import Base

# class PostLike(Base):
#     __tablename__ = 'postlikes'
#     id = Column(Integer, primary_key=True, index=True)
#     post_id = Column(Integer, ForeignKey('posts.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     created_at = Column(DateTime, default=datetime.utcnow)

#     post = relationship("Post", back_populates="likes")
#     user = relationship("User", back_populates="likes")

# 2. Update the `Post` and `User` Models to include relationships to PostLike:

# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True, index=True)
#     # other fields...
#     likes = relationship("PostLike", back_populates="post")

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     # other fields...
#     likes = relationship("PostLike", back_populates="user")

# #### b) User Should Be Able to 'Like' Posts

# 1. Endpoint to 'Like' a Post:
#    - Create an endpoint that allows users to like a post.
#    - Check that the user does not like their own post.

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from .database import get_db
# from .models import PostLike, Post, User
# from .schemas import PostLikeCreate
# from .auth import get_current_user

# router = APIRouter()

# @router.post("/posts/{post_id}/like")
# def like_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     if post.user_id == current_user.id:
#         raise HTTPException(status_code=400, detail="Users cannot like their own post")
#     like = db.query(PostLike).filter(PostLike.post_id == post_id, PostLike.user_id == current_user.id).first()
#     if like:
#         raise HTTPException(status_code=400, detail="Post already liked")
#     new_like = PostLike(post_id=post_id, user_id=current_user.id)
#     db.add(new_like)
#     db.commit()
#     db.refresh(new_like)
#     return new_like

# #### c) User Should Be Able to 'Unlike' Posts

# 1. Endpoint to 'Unlike' a Post:

# @router.delete("/posts/{post_id}/unlike")
# def unlike_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     like = db.query(PostLike).filter(PostLike.post_id == post_id, PostLike.user_id == current_user.id).first()
#     if not like:
#         raise HTTPException(status_code=400, detail="Like not found")
#     db.delete(like)
#     db.commit()
#     return {"message": "Like removed"}

# #### d) Update PostDisplay Schema to Show Number of Likes

# 1. Update Schema:

# from pydantic import BaseModel
# from typing import List

# class PostDisplay(BaseModel):
#     id: int
#     content: str
#     likes_count: int
#     liked_by_user: bool

#     class Config:
#         orm_mode = True

# 2. Update Endpoint to Calculate Likes Count:

# @router.get("/posts", response_model=List[PostDisplay])
# def get_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     posts = db.query(Post).all()
#     for post in posts:
#         post.likes_count = db.query(PostLike).filter(PostLike.post_id == post.id).count()
#         post.liked_by_user = db.query(PostLike).filter(PostLike.post_id == post.id, PostLike.user_id == current_user.id).first() is not None
#     return posts

# ### Frontend (React)

# #### f) Add Number of Likes for Each Post

# 1. Fetch and Display Posts:
#    - Fetch posts from the backend and display the number of likes.

# import React, { useEffect, useState } from 'react';
# import axios from 'axios';

# const PostList = () => {
#     const [posts, setPosts] = useState([]);

#     useEffect(() => {
#         axios.get('/api/posts')
#             .then(response => {
#                 setPosts(response.data);
#             })
#             .catch(error => {
#                 console.error("There was an error fetching the posts!", error);
#             });
#     }, []);

#     return (
#         <div>
#             {posts.map(post => (
#                 <div key={post.id}>
#                     <p>{post.content}</p>
#                     <p>{post.likes_count} Likes</p>
#                     <button>{post.liked_by_user ? 'Unlike' : 'Like'}</button>
#                 </div>
#             ))}
#         </div>
#     );
# };

# export default PostList;

# #### g) Add Way for User to Like/Unlike Post

# 1. Like/Unlike Button Logic:

# const toggleLike = (postId, likedByUser) => {
#     if (likedByUser) {
#         axios.delete(`/api/posts/${postId}/unlike`)
#             .then(() => {
#                 // Update the post state to reflect the unlike
#                 setPosts(posts.map(post => post.id === postId ? { ...post, liked_by_user: false, likes_count: post.likes_count - 1 } : post));
#             })
#             .catch(error => {
#                 console.error("There was an error unliking the post!", error);
#             });
#     } else {
#         axios.post(`/api/posts/${postId}/like`)
#             .then(() => {
#                 // Update the post state to reflect the like
#                 setPosts(posts.map(post => post.id === postId ? { ...post, liked_by_user: true, likes_count: post.likes_count + 1 } : post));
#             })
#             .catch(error => {
#                 console.error("There was an error liking the post!", error);
#             });
#     }
# };

# return (
#     <div>
#         {posts.map(post => (
#             <div key={post.id}>
#                 <p>{post.content}</p>
#                 <p>{post.likes_count} Likes</p>
#                 <button onClick={() => toggleLike(post.id, post.liked_by_user)}>
#                     {post.liked_by_user ? 'Unlike' : 'Like'}
#                 </button>
#             </div>
#         ))}
#     </div>
# );

# ### Summary

# - Backend: Define a PostLike model, endpoints to like/unlike posts, and update PostDisplay schema to include likes count and whether the user liked the post.
# - Frontend: Fetch and display posts with their likes count, and implement logic to like/unlike posts with UI updates.

# By following this plan, you can effectively integrate a 'like' system into your marketplace and social network application, enhancing user engagement and interaction.

# 4. The differences between these HTTP verbs are as below:
# - Post: We can create/post data to the server to be processed to a specified resource.
# URL: '/product/'
# return body: {...}
# response code: 201
# response body:{...}

# - Get: We can retrieve/read data from a server.
# URL: '/product/'  or  '/product/{id}'
# return body: -
# response code: 200
# response body:[{...} , {...} , {...} , ...]

# - Put: We can update a current resource with new data
# URL: '/product/{id}'
# return body: {...}
# response code: 200
# response body:{...}

# - Delete: We can delete/emove a specified resource.
# URL: '/product/{id}'
# return body: -
# response code: 204
# response body:-