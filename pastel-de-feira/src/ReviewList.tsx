import React from 'react';
import { Review } from './types';

interface ReviewListProps {
  reviews: Review[];
  onDelete: (title: string) => void;
  onEdit: (review: Review) => void;
}

const ReviewList: React.FC<ReviewListProps> = ({ reviews, onDelete, onEdit }) => (
  <ul>
    {reviews.map(review => (
      <li key={review.id}>
        {review.title} - {review.description} - {review.author} - {review.product}
        <button onClick={() => onEdit(review)}>Edit</button>
        <button onClick={() => onDelete(review.title)}>Delete</button>
      </li>
    ))}
  </ul>
);

export default ReviewList;