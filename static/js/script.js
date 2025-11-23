function openTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });

    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    document.getElementById('tab-' + tabName).classList.add('active');
    document.getElementById('btn-' + tabName).classList.add('active');
}

function updateFileName(input, spanId) {
    const fileName = input.files[0] ? input.files[0].name : "No file chosen";
    document.getElementById(spanId).textContent = fileName;
}

window.addEventListener('pageshow', function(event) {
    
    const imageInput = document.getElementById('imageInput');
    const imageSpan = document.getElementById('name-image');
    if (imageInput) { 
        imageInput.value = ''; // Kosongkan data file
        imageSpan.textContent = 'No file chosen'; // Reset teks label
    }

    // Reset Input Video
    const videoInput = document.getElementById('videoInput');
    const videoSpan = document.getElementById('name-video');
    if (videoInput) {
        videoInput.value = ''; // Kosongkan data file
        videoSpan.textContent = 'No file chosen'; // Reset teks label
    }
    
    // (Opsional) Reset Pilihan Dropdown Enhancement ke Default
    const selects = document.querySelectorAll('select');
    selects.forEach(select => select.selectedIndex = 0);
});
