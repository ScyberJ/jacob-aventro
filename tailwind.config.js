/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./jacob/**/*.{html, js}"],
  theme: {
    fontFamily: {
      inter: ["Inter"],
      lora: ["Lora"],
    },
    extend: {
      colors: {
        cardinal: {
          DEFAULT: "#bb1c41",
          100: "#25060d",
          200: "#4b0b1a",
          300: "#701127",
          400: "#951634",
          500: "#bb1c41",
          600: "#e0315a",
          700: "#e86583",
          800: "#f098ac",
          900: "#f7ccd6",
        },
        gray: {
          DEFAULT: "#7f7f7f",
          100: "#1a1a1a",
          200: "#333333",
          300: "#4d4d4d",
          400: "#666666",
          500: "#7f7f7f",
          600: "#999999",
          700: "#b3b3b3",
          800: "#cccccc",
          900: "#e6e6e6",
        },
      },
    },
  },
  plugins: [],
};
