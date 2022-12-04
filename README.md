
#  platform agrihack0x07
Forked from [CTFd/CTFd](https://github.com/CTFd/CTFd). Was made for Agrihack0x07 Qualification.

- Added `nama_lengkap`, `nim`, `angkatan`, `is_peserta` attributes to `users` table
- Disabled register
- Modified auth. ` If user is not exist in CTFd database, do a get request to IPB API to check if user exist in their database. If so, insert a new user. `
- Other minor frontend changes

## Contributors
- [Irfan Alamsyah](https://github.com/irfanalmsyah)
- [Patar Isac Pardomuan](https://github.com/patarisac)
