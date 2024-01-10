import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/react/20/solid";
import Link from "next/link";
const data = [
  {
    event: 1704963600000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
  {
    event: 1704960000000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
  {
    event: 1704956400000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
  {
    event: 1704952800000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
];
const data2 = [
  {
    event: 1704949200000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
  {
    event: 1704945600000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
  {
    event: 1704942000000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
  {
    event: 1704938400000,
    title: "Bản tin thị trường",
    detai:
      "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
  },
];
export default function Home() {
  return (
    <>
      <div className="w-full max-w-5xl flex flex-row mt-4 h-auto">
        <div className="w-1/2 flex flex-col h-auto">
          {data.map((item) => {
            const now = Date.now();
            const date = new Date(item.event);
            let interval = Math.trunc((now - date) / (1000 * 3600));
            return (
              <Link
                key={item.event}
                href={`/${item.event}`}
                className="w-full relative"
              >
                <div
                  className="absolute w-20 h-28 top-4 flex flex-col rounded-lg overflow-hidden"
                  style={{ backgroundColor: "#2b9797" }}
                >
                  <div className="flex-1 flex items-center justify-center text-white font-bold text-5xl">
                    {date.getHours()}
                  </div>
                  <div
                    className="w-full h-10 flex items-center justify-center text-white font-bold text-sm"
                    style={{ backgroundColor: "#01302a" }}
                  >
                    {date.getDate() +
                      "/" +
                      (date.getMonth() + 1) +
                      "/" +
                      date.getFullYear()}
                  </div>
                </div>
                <div
                  className="ml-10 pl-16 pr-4 text-white py-4"
                  style={{ backgroundColor: "#006464" }}
                >
                  <div className="font-semibold text-xl">{item.title}</div>
                  <div className="text-sm mt-3 flex-1">
                    {item.detai.slice(0, 200)}...
                  </div>
                  <div className="mt-2 text-xs text-gray-200">🕝 {interval} giờ trước</div>
                </div>
              </Link>
            );
          })}
        </div>
        <div className="w-1/2 ml-6 mb-10 flex flex-col">
          {data2.map((item, idx) => {
            const now = Date.now();
            const date = new Date(item.event);
            let interval = Math.trunc((now - date) / (1000 * 3600));
            return (
              <div key={item.event} className="w-full relative">
                <div
                  className="absolute w-20 h-28 top-4 flex flex-col rounded-lg overflow-hidden"
                  style={{ backgroundColor: "#2b9797" }}
                >
                  <div className="flex-1 flex items-center justify-center text-white font-bold text-5xl">
                    {date.getHours()}
                  </div>
                  <div
                    className="w-full h-10 flex items-center justify-center text-white font-bold text-sm"
                    style={{ backgroundColor: "#01302a" }}
                  >
                    {date.getDate() +
                      "/" +
                      (date.getMonth() + 1) +
                      "/" +
                      date.getFullYear()}
                  </div>
                </div>
                <div
                  className={`ml-10 pl-16 pr-4 text-black py-4 border-l border-r border-gray-400 ${
                    idx === data2.length - 1
                      ? "border-b"
                      : idx === 0 && "border-t"
                  }`}
                  style={{ backgroundColor: "#ffffff" }}
                >
                  <div className="font-semibold text-xl">{item.title}</div>
                  <div className="text-sm mt-3 flex-1">
                    {item.detai.slice(0, 200)}...
                  </div>
                  <div className="mt-2 text-xs text-gray-600">
                  🕝 {interval} giờ trước
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
      <div className="flex items-center justify-between border-t border-gray-200 bg-white px-4 py-3 sm:px-6">
        <div className="flex flex-1 justify-between sm:hidden">
          <a
            href="#"
            className="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
          >
            Previous
          </a>
          <a
            href="#"
            className="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
          >
            Next
          </a>
        </div>
        <div className="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
          <div>
            <nav
              className="isolate inline-flex -space-x-px rounded-md shadow-sm"
              aria-label="Pagination"
            >
              <a
                href="#"
                className="relative inline-flex items-center rounded-l-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                <span className="sr-only">Previous</span>
                <ChevronLeftIcon className="h-5 w-5" aria-hidden="true" />
              </a>
              {/* Current: "z-10 bg-indigo-600 text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600", Default: "text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:outline-offset-0" */}
              <a
                href="#"
                aria-current="page"
                className="relative z-10 inline-flex items-center bg-indigo-600 px-4 py-2 text-sm font-semibold text-white focus:z-20 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                1
              </a>
              <a
                href="#"
                className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                2
              </a>
              <a
                href="#"
                className="relative hidden items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0 md:inline-flex"
              >
                3
              </a>
              <span className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-700 ring-1 ring-inset ring-gray-300 focus:outline-offset-0">
                ...
              </span>
              <a
                href="#"
                className="relative hidden items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0 md:inline-flex"
              >
                8
              </a>
              <a
                href="#"
                className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                9
              </a>
              <a
                href="#"
                className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                10
              </a>
              <a
                href="#"
                className="relative inline-flex items-center rounded-r-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                <span className="sr-only">Next</span>
                <ChevronRightIcon className="h-5 w-5" aria-hidden="true" />
              </a>
            </nav>
          </div>
        </div>
      </div>
    </>
  );
}
