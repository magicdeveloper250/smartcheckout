`use strict`;

function convertDateTimeString(datetimeString) {
  const date = datetimeString.split("T")[0];
  const time = datetimeString.split("T")[1].split(".")[0];
  return `${date} ${time}`;
}

function actionsContainer() {
  let el = `
  <div class="btn-group" role="group">
    <button class="btn btn-outline-secondary"><i class="bi bi-eye"></i></button>
    <button class="btn btn-outline-secondary"><i class="bi bi-trash"></i></button>
  </div>`;
  return el;
}

function filterStatuses(orders=[]){
  let processing= orders.filter(order=>order.status=="Processing").length
  let completed=orders.filter(order=>order.status=="Completed").length
  let cancelled=orders.filter(order=>order.status=="Cancelled").length
  return [processing, completed, cancelled]
}

function generateStatuses(orders){
  const[processing, completed, cancelled]= filterStatuses(orders)
  const el=`
    <button class="btn btn-outline-secondary">Completed<span class="fw-bold">(${completed})</span></button>
    <button class="btn btn-outline-secondary"> Processing<span class="fw-bold">(${processing})</span></button>
    <button class="btn btn-outline-secondary"> Cancelled<span class="fw-bold">(${cancelled})</span></button>
    `
  return el
}
function generateOrders(orders) {
  let el = ``;
  orders.forEach((order) => {
    el += `<tr>
          <td>${order.id}</td>
          <td>${order.cust_id}</td>
          <td>${convertDateTimeString(order.time)}</td>
          <td>${order.status}</td>
          <td>${order.value}</td>`;
    el += `<td>`;
    el += actionsContainer();
    el += `</td>`;
    el += `</tr>`;
  });
  return el;
}

function Orders() {
  const getOrders = async () => {
    try {
      const resp = await fetch("/api/order", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await resp.json();
      if (resp.ok) {
        document.querySelector(".orders-container tbody").innerHTML =
          generateOrders(data.data);
        document.querySelector(".status-container").innerHTML=generateStatuses(data.data);
      }
    } catch (err) {
      console.log(String(err));
    }
  };
  getOrders();

  return `
  <div class="orders-container">
    <h1 class="h1 text-strong"> Orders</h1>
    <div class="search-box">
    <i class="bi bi-search"></i>
    <input type="text" class="search-input" placeholder="search order"/>
    </div>
    <div class="btn-group status-container" role="group">
    
  </div>
     <table id="ordersTable">
      <thead>
        <tr>
          <th>Order Id</th>
          <th>Customer id</th>
          <th>Time</th>
          <th>Status</th>
           <th>Value</th>
           <th>Actions</th>
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>
  </div>`;
}

export default Orders;
