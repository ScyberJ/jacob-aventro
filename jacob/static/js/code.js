window.addEventListener("load", () => {
  const details = document.querySelectorAll(".bdc-details");

  for (let index = 0; index < details.length; index++) {
    const element = details[index];

    const getOpenDetails = () => document.querySelectorAll("details.bdc-details[open]"); 

    element.addEventListener("toggle", () => {
      if (element.open) {
        for (let openDetail of getOpenDetails()) {
            if (element !== openDetail){
                delete openDetail.removeAttribute("open");
            }
        }
      }
    });
  }
});
