`use strict`;
function renderCarts(carts) {
  const cartsTable = document.querySelector(".carts-container tbody");
  let el = ``;
  carts.forEach((cart) => {
    el += `<tr>
              <td>${cart.id}</td>`;
    el += `<td>`;
    // el += ` <details>
    //             <summary> Products</summary>`;
    cart.products.forEach((product) => {
      el += ` 
              <ul>
                  <li>${product.id}</li>
                  <li>${product.name}</li>
                  <li>${product.price}</li>
              </ul>    
      `;
    });
    // el += `</details>`;
    el += `</td>`;
    el += `</tr>`;
  });
  cartsTable.innerHTML = el;
}
function Carts() {
  let apps = [];
  let carts = [];
  const socket = new WebSocket(`ws://${window.location.host}/cart`);
  socket.addEventListener("open", (event) => {
    socket.send(
      JSON.stringify({
        action: "all",
      })
    );
  });
  socket.addEventListener("message", (event) => {
    const data = JSON.parse(event.data);
    switch (data?.type) {
      case "all":
        apps = data.apps;
        apps.map((app) => {
          carts.push(app.cart);
        });
        break;
      case "cart":
        carts.map((cart, index) => {
          if (cart.id == data.cart.id) {
            carts[index] = data.cart;
          }
        });
        break;
      case "remove":
        carts.map((cart, index) => {
          if (cart.id == data.cart.id) {
            carts[index] = data.cart;
          }
        });
        break;
      case "update":
        carts.map((cart, index) => {
          if (cart.id == data.cart.id) {
            carts[index] = data.cart;
          }
        });
        break;
    }
    renderCarts(carts);
  });
  socket.addEventListener("close", (event) => {
    console.log("disconnected");
  });
  return `
  <div class="carts-container">
   
      <h1 class="h1 text-strong"> Carts</h1>
      <div class="search-box">
      <i class="bi bi-search"></i>
      <input type="text" class="search-input" placeholder="search cart"/>
      </div>
     <table id="cartsTable">
      <thead>
        <tr>
          <th>Cart id</th>
          <th>Products</th>
           
        </tr>
      </thead>
      <tbody>
        <!-- Dynamic rows will be inserted here -->
      </tbody>
    </table>
  </div>`;
}

export default Carts;
