Vue.component('product', {
	props: {
		premium: {
			type: Boolean,
			required: true
		}
	},
	template: `
	<div class="product">
	<div class="product-image">
		<img v-bind:src="image">
	</div>

	<div class="product-info">
		<h1>{{ title }}</h1>
		<p v-if="inStock">In Stock</p>
		<p v-else="inStock" :class="{ lineThrough: !inStock }">Out of Stock</p>
		<p v-show="onSale">On Sale - {{ title }}</p>
		<p>{{ sale }}</p>
		<p>User is premium: {{ premium }}</p>
		<p>Shipping : {{shipping}}</p>
	</div>

	<ul>
		<li v-for="detail in details"> {{ detail }}</li>
	</ul>

	<div v-for="(variant, index) in variants"
	 :key="variant.variantId"
	 class="color-box"
	 :style="{ backgroundColor: variant.variantColor }"
	 @mouseover="updateProduct(index)">
	</div>

	<ul>
		<li v-for="size in sizes"> {{ size }}</li>
	</ul>

	<button v-on:click="addToCart" 
	:disabled="!inStock"
	:class="{ disabledButton: !inStock }">Add To Cart</button>

	<button @click="removeFromCart">Remove From Cart</button>

	<div>
	<h2>Reviews</h2>
	<p v-if="!reviews.length">There are no reviews yet</p>
	<ul>
	<li v-for="review in reviews">
	<p>{{ review.name }}</p>
	<p>Rating: {{ review.rating }}</p>
	<p>{{ review.review }}</p>
	<p v-if="review.recommend === 'yes'">You would recommend to a friend</p>
	<p v-else-if="review.recommend === 'no'">You would not recommend to a friend</p>
	</li>
	</ul>
	</div>

	<product-review @review-submitted="addReview"></product-review>
</div>
`,
	data() {
		return {
			brand: 'Vue Mastery',
			product: 'Socks',
			selectedVariant: 0,
			onSale: true,
			details: ["80% cotton", "20% polyester", "Gender-neutral"],
			variants: [{
					variantId: 2234,
					variantColor: "green",
					variantImage: "socks.jpg",
					variantQuantity: 10
				},
				{
					variantId: 2235,
					variantColor: "blue",
					variantImage: "socks-blue.jpg",
					variantQuantity: 12
				}
			],
			sizes: ["Large", "Medium", "Small"],
			reviews: []
		}
	},
	methods: {
		addToCart() {
			this.$emit('add-to-cart', this.variants[this.selectedVariant].variantId);
		},
		removeFromCart() {
			this.$emit('remove-from-cart', this.variants[this.selectedVariant].variantId);
		},
		updateProduct(index) {
			this.selectedVariant = index;
		},
		addReview(productReview) {
			this.reviews.push(productReview);
		}
	},
	computed: {
		title() {
			return this.brand + ' ' + this.product;
		},
		image() {
			return this.variants[this.selectedVariant].variantImage;
		},
		inStock() {
			return this.variants[this.selectedVariant].variantQuantity;
		},
		sale() {
			if (this.onSale) {
				return this.brand + ' ' + this.product + ' are on sale!';
			}
			return this.brand + ' ' + this.product + ' are not on sale';
		},
		shipping() {
			if (this.premium) {
				return "Free";
			}
			return 2.99;
		}
	}
})

Vue.component('product-review', {
	template: `
	<form class="review-form" @submit.prevent="onSubmit">

	<p v-if="errors.length">
	Please correct the following error(s):
	<ul>
	<li v-for="error in errors">{{ error }}</li>
	</ul
	</p>

      <p>
        <label for="name">Name:</label>
        <input id="name" v-model="name" placeholder="name">
      </p>
      
      <p>
        <label for="review">Review:</label>      
        <textarea id="review" v-model="review"></textarea>
      </p>
      
      <p>
        <label for="rating">Rating:</label>
        <select id="rating" v-model.number="rating">
          <option>5</option>
          <option>4</option>
          <option>3</option>
          <option>2</option>
          <option>1</option>
        </select>
	  </p>
	  
	<p>Would you recommend this product?</p>
	<input type="radio" id="recommend" value="yes" v-model="recommend"> Yes<br>
	<input type="radio" id="recommend" value="no" v-model="recommend"> No<br>
          
      <p>
        <input type="submit" value="Submit">  
      </p>    
    
    </form>
	`,
	data() {
		return {
			name: null,
			review: null,
			rating: null,
			recommend: null,
			errors: []
		}
	},
	methods: {
		onSubmit() {
			if (this.name && this.review && this.rating && this.recommend === 'yes') {
				let productReview = {
					name: this.name,
					review: this.review,
					rating: this.rating,
					recommend: this.recommend
				}
				this.$emit('review-submitted', productReview);
				this.name = null,
					this.review = null,
					this.rating = null,
					this.recommend = null
			} else {
				if (!this.name) this.errors.push("Name required");
				if (!this.review) this.errors.push("Review required");
				if (!this.rating) this.errors.push("Rating required");
				if(this.recommend != 'yes') this.errors.push("You have to recommend this product to a friend");
			}
		}
	}
})

var app = new Vue({
	el: '#app',
	data: {
		premium: true,
		cart: []
	},
	methods: {
		updateCart(id) {
			this.cart.push(id);
		},
		removeFromCart(id) {
			this.cart.splice(this.cart.indexOf(id), 1);
		}
	}
});