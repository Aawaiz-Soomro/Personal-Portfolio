from flask import Flask, url_for


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    from .routes import bp as portfolio_bp

    app.register_blueprint(portfolio_bp)

    @app.route("/")
    def index():
        return (
            "<p>You're home. Visit the "
            f"<a href='{url_for('portfolio.portfolio')}'>portfolio</a> to explore the site.</p>"
        )

    return app
