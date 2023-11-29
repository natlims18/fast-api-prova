import React, { useState, useEffect } from 'react';
import axios from 'axios'
import ReviewForm from './ReviewForm';
import ReviewList from './ReviewList';
import { Review } from './types';

const App: React.FC = () => {
  const [reviews, setReviews] = useState<Review[]>([]);
  const [selectedReview, setSelectedReview] = useState<Review | undefined>();

  const fetchReviews = async () => {
    const response = await axios.get('http://localhost:8000/list');
    setReviews(response.data);
  };

  const handleEdit = (review: Review) => {
    setSelectedReview(review);
  };


  useEffect(() => {
    fetchReviews();
  }, []);

  const handleDelete = async (title: string) => {
    await axios.delete(`http://localhost:8000/delete?title=${title}`);
    fetchReviews();
  };

  return (
    <div>
      <ReviewForm onSubmit={fetchReviews} review={selectedReview} />
      <ReviewList reviews={reviews} onDelete={handleDelete} onEdit={handleEdit} />
    </div>
  );
};
export default App;