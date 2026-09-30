import React from 'react';

export default function WhatsAppButton() {
  const whatsappUrl = "https://wa.me/919422035109?text=Hello%20CyTOS%20Team%2C%20I%20am%20interested%20in%20your%20CNC%20and%20Automation%20Machines.%20Please%20share%20details.";

  return (
    <a
      href={whatsappUrl}
      target="_blank"
      rel="noopener noreferrer"
      className="whatsapp-float-btn"
      aria-label="Chat with CyTOS engineering team on WhatsApp"
      title="Chat on WhatsApp"
    >
      <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor">
        <path d="M12.031 2C6.495 2 2 6.495 2 12.031c0 1.954.557 3.784 1.521 5.337L2 22l4.808-1.503a9.983 9.983 0 0 0 5.223 1.534h.005c5.535 0 10.03-4.495 10.03-10.031C22.066 6.495 17.571 2 12.031 2zm5.834 14.195c-.244.685-1.42 1.309-1.958 1.393-.513.08-1.182.115-1.914-.12-.444-.143-1.015-.333-1.748-.654-3.087-1.353-5.105-4.475-5.26-4.68-.154-.206-1.258-1.674-1.258-3.193 0-1.52.793-2.268 1.074-2.576.282-.308.615-.385.82-.385.205 0 .41.002.59.01.19.01.446-.072.697.533.256.615.872 2.128.949 2.282.077.154.128.333.026.539-.103.205-.154.333-.308.513-.154.18-.323.4-.462.538-.154.154-.314.323-.135.63.18.308.798 1.318 1.713 2.133 1.176 1.048 2.167 1.373 2.475 1.527.308.154.487.128.667-.077.18-.205.769-.897.974-1.205.205-.308.41-.256.692-.154.282.103 1.794.846 2.102 1.001.308.154.513.23.59.359.077.128.077.744-.167 1.429z" />
      </svg>
      <span className="whatsapp-float-label">Chat with Us</span>
    </a>
  );
}
