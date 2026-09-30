import React from 'react';
import { useParams, Navigate } from 'react-router-dom';
import HtmlPageWrapper from '../components/HtmlPageWrapper';
import { allBlogsHtml } from '../data/allBlogsHtml';

export default function BlogPostPage() {
  const { slug } = useParams();
  const article = allBlogsHtml[slug];

  if (!article) {
    return <Navigate to="/blog" replace />;
  }

  return (
    <HtmlPageWrapper
      htmlContent={article.html}
      title={article.title}
      description={article.description}
    />
  );
}
