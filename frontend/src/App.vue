<template>

	<div id="wrapper">

		<nav class="navbar is-dark">
			<div class="container">
				<div class="navbar-brand">

					<router-link to="/" class="navbar-item brand-text"><strong>Tech Co</strong></router-link>
					<a class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navMenu">
                    	<span aria-hidden="true"></span>
                    	<span aria-hidden="true"></span>
                    	<span aria-hidden="true"></span>
                	</a>
            	</div>

				<div id="navMenu" class="navbar-menu">

					<div class="navbar-start">
						<router-link to="/catalogue" class="navbar-item">Catalogue</router-link>
						<router-link to="/orders" class="navbar-item">Orders</router-link>
						<router-link to="/inventory" class="navbar-item">Inventory</router-link>
						<router-link to="/kpi" class="navbar-item">KPI</router-link>
            	    </div>
					<div class="navbar-end">
						<div class="navbar-item">
							<div class="buttons">
								<router-link to="/log-in" class="button is-light">Log In</router-link>
								<router-link to="/cart" class="button is-success">
									<span class="icon"><font-awesome-icon icon="fa-solid fa-shopping-cart"/></span>
									<span>Cart</span>
								</router-link>
							</div>
						</div>
            	    </div>

				</div>
			</div>
		</nav>

		<div class="container">
			<router-view/>
		</div>

	</div>

</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
