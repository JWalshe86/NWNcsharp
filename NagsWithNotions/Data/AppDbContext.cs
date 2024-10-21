using Microsoft.EntityFrameworkCore;
using NagsWithNotions.Models;
using NagsWithNotions.Models; // Change this to your actual namespace

namespace NagsWithNotions.Data  // Change to your actual namespace
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options)
            : base(options)
        {
        }

        public DbSet<Event> Events { get; set; } // DbSet for Event model

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // You can configure the model here if needed
            base.OnModelCreating(modelBuilder);
        }
    }
}
