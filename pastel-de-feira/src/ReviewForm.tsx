import React, { useState } from 'react';
import axios from 'axios';
import { Review } from './types';

interface ReviewFormProps {
  onSubmit: () => void;
  review?: Review; // Optional for update
}

const ReviewForm: React.FC<ReviewFormProps> = ({ onSubmit, review }) => {
  const [title, setTitle] = useState(review?.title || '');
  const [description, setDescription] = useState(review?.description || '');
  const [author, setAuthor] = useState(review?.author || '');
  const [product, setProduct] = useState(review?.product || '');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const data = { title, description, author, product };
    if (review) {
      await axios.put(`http://localhost:8000/review/update?title=${title}`, data);
    } else {
      await axios.post(`http://localhost:8000/review/create/`, data);
    }
    setTitle('');
    setDescription('');
    setAuthor('');
    setProduct('');
    onSubmit();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={title} onChange={e => setTitle(e.target.value)} placeholder="Titulo" />
      <input type="text" value={description} onChange={e => setDescription(e.target.value)} placeholder="Descrição" />
      <input type="text" value={author} onChange={e => setAuthor(e.target.value)} placeholder="Autor" />
      <input type="text" value={product} onChange={e => setProduct(e.target.value)} placeholder="Produto" />
      <button type="submit">{review ? 'Update' : 'Create'}</button>
    </form>
  );
};

export default ReviewForm;