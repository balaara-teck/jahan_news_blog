// Function to get formatted share content
function getShareContent() {
    const title = document.querySelector('.text-start.text-muted').textContent.trim();
    const url = window.location.href;
    return {
        title: encodeURIComponent(title),
        url: encodeURIComponent(url)
    };
}

// Function to share on Facebook
function shareOnFacebook() {
    const { url, title } = getShareContent();
    const shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}&quote=${title}`;
    window.open(shareUrl, '_blank');
}

// Function to share on Twitter
function shareOnTwitter() {
    const { url, title } = getShareContent();
    const shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
    window.open(shareUrl, '_blank');
}

// Function to share on WhatsApp
function shareOnWhatsApp() {
    const { url, title } = getShareContent();
    const shareUrl = `https://api.whatsapp.com/send?text=${title}%0A%0A${url}`;
    window.open(shareUrl, '_blank');
}

// Function to copy link to clipboard
function copyLink() {
    const { url, title } = getShareContent();
    const textToCopy = `${decodeURIComponent(title)}\n${decodeURIComponent(url)}`;
    
    navigator.clipboard.writeText(textToCopy).then(() => {
        const copyBtn = document.getElementById('copyLinkBtnFloat');
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="bi bi-check"></i> Copied!';
        setTimeout(() => {
            copyBtn.innerHTML = originalText;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
        alert('Failed to copy link');
    });
}
