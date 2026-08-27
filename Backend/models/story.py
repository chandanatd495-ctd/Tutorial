
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean,JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base
class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    
    created_at = Column(DateTime, server_default=func.now())


    nodes=relationship("StoryNode",back_populates="story")

class StoryNode(Base):
    __tablename__ = "story_nodes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    story_id = Column(String, ForeignKey("stories.id"),index=True)
    is_root = Column(Boolean, default=False)
    is_end = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON,default=list)
    

    story=relationship("Story",back_populates="nodes")