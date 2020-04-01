# Django Project - Review App

> 진행하며 어려웠던 점

- 아직까지는 없었다...! 
  - 명세에 있는 내용까지는 완성해서 일단 지금 push하고, `Update` 와 `Delete` 기능을 추가할 예정이다. 
    - 추가하고 더 추가하고 싶어서 `Search` 기능을 추가했다. 너무 재밌다.

<br>

#### Features

- `Update` 
  - **Jquery** 를 사용하여 `<span>` tag 를 `<input>` 과 `<textarea>` 로 바꾸어 구현했다
- `Delete`
  - **Modal**을 활용하여 삭제 전 confirm 하는 창을 만들어 구현했다
- `Search`
  - **Django**의 `Entry.object.filter()` method를 활용하여 구현했다