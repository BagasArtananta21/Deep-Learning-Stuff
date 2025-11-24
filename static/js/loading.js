function openTab(tabName) {
        document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));

        document.getElementById('tab-' + tabName).classList.add('active');
        document.getElementById('btn-' + tabName).classList.add('active');
    }

    function updateFileName(input, spanId) {
        const fileName = input.files[0] ? input.files[0].name : "No file chosen";
        document.getElementById(spanId).innerText = fileName;
    }

    const videoForm = document.getElementById('videoForm');
    const progressContainer = document.getElementById('progress-container');
    const progressBar = document.getElementById('progressBar');
    const statusText = document.getElementById('statusText');
    const btnUploadVideo = document.getElementById('btnUploadVideo');

    videoForm.addEventListener('submit', function(e) {
        e.preventDefault(); 

        const fileInput = document.getElementById('videoInput');
        if (fileInput.files.length === 0) {
            alert("Pilih video terlebih dahulu!");
            return;
        }

        progressContainer.style.display = 'block';
        btnUploadVideo.style.display = 'none'; 

        const formData = new FormData(videoForm);
        const xhr = new XMLHttpRequest();

        xhr.upload.addEventListener('progress', function(e) {
            if (e.lengthComputable) {
                const percentComplete = Math.round((e.loaded / e.total) * 100);
                progressBar.style.width = percentComplete + '%';
                progressBar.innerText = percentComplete + '%';

                if (percentComplete === 100) {
                    statusText.innerText = "Upload Selesai. Sedang Memproses tunggu hingga selesai";
                    progressBar.style.background = "#22c55e"; 
                }
            }
        });

        xhr.addEventListener('load', function() {
            if (xhr.status === 200) {
                document.open();
                document.write(xhr.responseText);
                document.close();
            } else {
                alert("Terjadi kesalahan saat memproses video.");
                progressContainer.style.display = 'none';
                btnUploadVideo.style.display = 'inline-block';
            }
        });

        xhr.addEventListener('error', function() {
            alert("Gagal mengupload video.");
            progressContainer.style.display = 'none';
            btnUploadVideo.style.display = 'inline-block';
        });

        xhr.open('POST', "/detectVideo");
        xhr.send(formData);
    });