// 2024-06-18T23:01:52.988881Z
export function convertDateTimeString(datetimeString) {
  const date = datetimeString.split("T")[0];
  const time = datetimeString.split("T")[1].split(".")[0];
  return `${date} ${time}`;
}
