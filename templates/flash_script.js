<script>
  // Function to remove flash messages after a delay
  setTimeout(function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
      message.parentElement.style.display = 'none';
    });
  }, 5000);
</script>