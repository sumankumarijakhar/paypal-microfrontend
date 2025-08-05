document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("paypal-button");

  if (btn) {
    btn.addEventListener("click", () => {
      console.log("✅ PayPal button clicked! Tracing simulated.");
      alert("Payment simulated! (This is a demo for tracing.)");
    });
  } else {
    console.error("Button not found.");
  }
});
