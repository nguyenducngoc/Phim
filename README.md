# Chào các bạn!!!
<br/>
<div align="center">
<img src="https://github.com/nguyenducngoc/Phim/blob/main/flyers/django-logo-positive.png" alt="nguyenducngoc" />
</div>
<br/>

Dự án website xem phim bằng **Django** 4.1.7 

# List to do:
Website hoàn chỉnh, tối ưu, cân bằng tải tốt nhất bằng Django.:


# Story User:

+ Các tác vụ liên quan đến Users(5 điểm)
+ Các tác vụ, phân loại Moive(10 điểm)
+ Chức năng tìm kiếm(4 điểm)
+ Thu thập dữ liệu phim(4 điểm)
+ Temp thân thiện, phù hợp xu hướng(5 điểm)
+ Quản lí thông tin bài viết (3 điểm)
+ Trang quản trị đơn giản dễ sử dụng(2 điểm)
## Phân tích thiết kế hệ thống
#### Bước 1: Xác định yêu cầu

Định rõ yêu cầu chức năng và phi chức năng của hệ thống. Ví dụ: Đăng nhập, tìm kiếm phim, xem thông tin phim, xem phim trực tuyến, đánh giá và bình luận phim, v.v.

#### Bước 2: Thiết kế cơ sở dữ liệu

Xác định các bảng dữ liệu cần thiết như Bảng Phim, Bảng Người dùng, Bảng Tin tức, v.v.
Thiết kế mối quan hệ giữa các bảng và quy định khóa ngoại.

#### Bước 3: Xác định mô hình dữ liệu

Xác định các mô hình dữ liệu trong Django, tương ứng với các bảng đã thiết kế.

#### Bước 4: Thiết kế giao diện người dùng

Tạo các trang mẫu (templates) cho các chức năng như trang chủ, tìm kiếm, xem phim, v.v.
Xây dựng giao diện người dùng responsive và hấp dẫn sử dụng HTML, CSS và JavaScript.

#### Bước 5: Xây dựng hệ thống xử lý

Tạo các view (điều khiển) trong Django để xử lý các yêu cầu từ người dùng.
Xây dựng các hàm xử lý trong view, lấy dữ liệu từ cơ sở dữ liệu và gửi nó đến các template để hiển thị.

#### Bước 6: Xác thực và phân quyền

Cài đặt hệ thống xác thực và phân quyền sử dụng Django Authentication và Authorization để đảm bảo chỉ người dùng đăng nhập mới có thể xem phim và thực hiện các hoạt động khác.

#### Bước 7: Tối ưu hóa hiệu suất và bảo mật

Tối ưu hóa truy vấn cơ sở dữ liệu để đảm bảo hiệu suất tốt.


#### Bước 8: Kiểm thử và triển khai

Thực hiện kiểm thử chức năng và hiệu suất để đảm bảo hệ thống hoạt động đúng và mượt mà.
Triển khai hệ thống lên môi trường sản phẩm, chuẩn bị cho việc triển khai thực tế.


## Sprint thứ I ( 8/3/2023 -> 14/3/2023): *Hoàn thành các tác vụ của User*

### Log Sprint

#### User

| TT  | Công việc | Thời gian thực hiện (giờ) | 
| ------------- | ------------- | ------------- | 
| 1  | Phân tích dữ liệu cho User  | 0.5  | 1  | | x | 
| 2  | Tạo dữ liệu mẫu cho User  | 0.5  | 1  | x| x | 
| 3  | Lập trình lấy dữ liệu  | 0.5  | 1  | x| x | 
| 4  | Thêm Sửa Xóa User  | 0.5  | 1  |x |  | 
| 5  | Test User  | 0.5  | 1  | x| x | 

## Sprint thứ II ( 15/3/2023 -> 28/3/2023): *Quản lí thông tin Phim*
#### Movie

| TT  | Công việc | Thời gian thực hiện (giờ) |  Nguyễn Đức Ngọc | Bùi Xuân Ngọc | 
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| 1  | Phân tích dữ liệu cho Movies  | 2  | x | x | 
| 2  | Tạo dữ liệu mẫu cho Movies  | 5  | x | x |
| 3  | Lập trình lấy dữ liệu  | 5 | x | |
| 4  | Thêm Sửa Xóa Movies  | 0.5  | x |  |
| 5  | Add Template  | 3  | x |  |
| 6  | Đổ dữ liệu  | 2  | x |x |
| 7  | Test Movies  | 5  | x | x |

 ## Sprint thứ III ( 28/3/2023 -> 15/4/2023): *Công vụ Tìm kiếm*
#### Công cụ tìm kiếm

| TT  | Công việc | Thời gian thực hiện (giờ) |  Nguyễn Đức Ngọc | Bùi Xuân Ngọc | 
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| 3  | Lập trình   | 5 | x | |
| 5  | Add Template  | 3  | x |x|
| 6  | Đổ dữ liệu  | 2  | x |x |
| 7  | Test   | 5  | x | x |

 ## Sprint thứ IV ( 15/4/2023 -> 25/4/2023): *Thu thập dữ liệu*
#### Thu thập dữ liệu

| TT  | Công việc | Thời gian thực hiện (giờ) |  Nguyễn Đức Ngọc | Bùi Xuân Ngọc | 
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| 3  | Lập trình  | 5 | x | |
| 5  | Add Template  | 1  | x |x|
| 6  | Đổ dữ liệu  | 2  | x |x |
| 7  | Test   | 5  | x | x |


#### Actor
| TT  | Công việc | Thời gian thực hiện (giờ) | 
| ------------- | ------------- | ------------- | 
| 1  | Phân tích dữ liệu cho Actor  | 0.5  |
| 2  | Tạo dữ liệu mẫu cho Actor | 0.5  |
| 3  | Lập trình lấy dữ liệu  | 1 |
| 4  | Thêm Sửa Xóa Actor  | 0.5  |
| 5  | Add Template  | 0.5  |
| 6  | Đổ dữ liệu  | 0.5  |
| 7  | Test Movies  | 0.5  |

 ## Sprint thứ V ( 15/4/2023 -> 25/4/2023): *Quản lí thông tin tin tức*
#### Quản lí thông tin bài viết

| TT  | Công việc | Thời gian thực hiện (giờ) |  Nguyễn Đức Ngọc | Bùi Xuân Ngọc | 
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| 1  | Phân tích dữ liệu cho News  | 2  | x | x | 
| 2  | Tạo dữ liệu mẫu cho News  | 5  | x | x |
| 3  | Lập trình lấy dữ liệu  | 5 | x | |
| 4  | Thêm Sửa Xóa News  | 0.5  | x |  |
| 5  | Add Template  | 3  | x |  |
| 6  | Đổ dữ liệu  | 2  | x |x |
| 7  | Test Movies  | 5  | x | x |
____




#### Tông quan Sprint 
| TT  | Sprints | Thời gian(h)  | Sản phẩm  | 
| ------------- | ------------- | ------------- | ------------- | 
| 1  | Sprint thứ 1: Tác vụ User  | 3  | Đăng nhập, đăng kí, đăng xuất  |
| 2  | Sprint thứ 2: Hoàn thiện thông tin Phim | 24  | Thành công lưu trữ thông tin phim |
| 3  | Sprint thứ 3: Công cụ tìm kiếm | 24  |Hoàn thành công cụ tìm kiếm |
| 4  | Sprint thứ 4: Thu thập dữ liệu | 24  |Hoàn thành thu thập dữ liệu |
| 5  | Sprint thứ 5: Quản lí thông tin tin tức | 24  |Thành công lưu trữ thông tin tin tức|
| 6  | Sprint thứ 6: Cải thiện trải nghiệm người dùng trên website | 24  | |


              

              
              
              


