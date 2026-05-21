import { useState } from 'react';
import api from '../api/axios';
import './PhotoDetailModal.css';

export default function PhotoDetailModal({ photo, onClose, onDelete }) {
    const [deleting, setDeleting] = useState(false);
    const [error, setError] = useState(null);

    const handleDelete = async () => {
        if (!window.confirm('Delete this photo? This cannot be undone.')) return;
        setDeleting(true);
        try {
            await api.delete(`/photos/${photo._id}`);
            onDelete(photo._id);
        } catch (err) {
            setError('Failed to delete photo.');
            setDeleting(false);
        }
    };

    const handleBackdropClick = (e) => {
        if (e.target === e.currentTarget) onClose();
    };

    return (
        <div className="modal-backdrop" onClick={handleBackdropClick}>
            <div className="modal-container">
                <button className="modal-close" onClick={onClose} aria-label="Close">✕</button>

                <img
                    src={photo.imageUrl}
                    alt={photo.caption || 'Photo'}
                    className="modal-image"
                />

                <div className="modal-details">
                    {photo.caption && (
                        <p className="modal-caption">{photo.caption}</p>
                    )}

                    <div className="modal-meta">
                        <span className="modal-meta-label">📍 Location</span>
                        <span>{photo.location.lat.toFixed(4)}, {photo.location.lng.toFixed(4)}</span>
                    </div>

                    <div className="modal-meta">
                        <span className="modal-meta-label">📅 Date</span>
                        <span>{new Date(photo.createdAt).toLocaleDateString('en-US', {
                            year: 'numeric', month: 'long', day: 'numeric'
                        })}</span>
                    </div>

                    {photo.tags && photo.tags.length > 0 && (
                        <div className="modal-tags">
                            {photo.tags.map((tag, i) => (
                                <span key={i} className="tag">{tag}</span>
                            ))}
                        </div>
                    )}

                    {error && <p className="modal-error">{error}</p>}

                    <button
                        className="modal-delete-btn"
                        onClick={handleDelete}
                        disabled={deleting}
                    >
                        {deleting ? 'Deleting...' : 'Delete Photo'}
                    </button>
                </div>
            </div>
        </div>
    );
}
