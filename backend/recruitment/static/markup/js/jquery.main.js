(function() {
	initBurgerMenu('.menu__opener', 'nav--active')
	initBurgerMenu('.search__opener', 'search--active')
	initBurgereMenu('.dropdown__opener', 'dropdown--active')
})()


function initBurgerMenu(selector, activeClass = 'active') {
	var isOpen = false
	var body = document.querySelector('body')

	document.querySelectorAll(selector)
	.forEach(function(menuLink) {
		menuLink.addEventListener('click', function(event) {
			event.preventDefault()

			if(isOpen)
				body.classList.remove(activeClass)
			else
				body.classList.add(activeClass)

			isOpen = !isOpen
		})
	})
}